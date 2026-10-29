/* ToolsRhino — interactions
   Everything degrades gracefully: with JS off, all content stays visible. */
(function () {
  'use strict';
  var doc = document, root = doc.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- sticky nav state ---------- */
  var shell = doc.querySelector('.nav-shell');
  function onScroll() { if (shell) shell.classList.toggle('scrolled', window.scrollY > 24); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- mobile menu ---------- */
  var burger = doc.querySelector('.burger'), mobile = doc.querySelector('.mobile');
  function setMenu(open) {
    if (!burger || !mobile) return;
    burger.setAttribute('aria-expanded', open);
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    mobile.classList.toggle('open', open);
    doc.body.classList.toggle('lock', open);
  }
  if (burger) {
    burger.addEventListener('click', function () { setMenu(burger.getAttribute('aria-expanded') !== 'true'); });
    mobile.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1060) setMenu(false); });
  }

  /* ---------- reveal on scroll ---------- */
  var revealEls = [].slice.call(doc.querySelectorAll('.reveal'));
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else { revealEls.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- cursor light on cards ---------- */
  doc.addEventListener('pointermove', function (e) {
    var c = e.target.closest && e.target.closest('.card');
    if (!c) return;
    var r = c.getBoundingClientRect();
    c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    c.style.setProperty('--my', (e.clientY - r.top) + 'px');
  }, { passive: true });

  /* ---------- scramble headings (text is real; effect is cosmetic) ---------- */
  var glyphs = '01<>/\\_—+=*#';
  function scramble(el) {
    if (reduce || el.__done) return; el.__done = true;
    var final = el.textContent, len = final.length, frame = 0, total = 26;
    var nodes = el.childNodes.length === 1 && el.firstChild.nodeType === 3;
    if (!nodes) return; // only plain-text headings
    var iv = setInterval(function () {
      var out = '';
      for (var i = 0; i < len; i++) {
        var ch = final[i];
        if (ch === ' ' || i < (frame / total) * len) out += ch;
        else out += glyphs[Math.floor(Math.random() * glyphs.length)];
      }
      el.textContent = out;
      if (++frame > total) { clearInterval(iv); el.textContent = final; }
    }, 28);
  }
  var scr = [].slice.call(doc.querySelectorAll('[data-scramble]'));
  if ('IntersectionObserver' in window && scr.length) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { scramble(en.target); so.unobserve(en.target); } });
    }, { threshold: 0.6 });
    scr.forEach(function (el) { so.observe(el); });
  }

  /* ---------- tabs ---------- */
  [].forEach.call(doc.querySelectorAll('[data-tabs]'), function (wrap) {
    var tabs = [].slice.call(wrap.querySelectorAll('[role="tab"]'));
    var panels = [].slice.call(wrap.querySelectorAll('[role="tabpanel"]'));
    function select(i, focus) {
      tabs.forEach(function (t, k) {
        t.setAttribute('aria-selected', k === i); t.tabIndex = k === i ? 0 : -1;
        panels[k].classList.toggle('on', k === i); panels[k].hidden = k !== i;
      });
      if (focus) tabs[i].focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') select((i + 1) % tabs.length, true);
        if (e.key === 'ArrowLeft') select((i - 1 + tabs.length) % tabs.length, true);
      });
    });
    select(0);
  });

  /* ---------- count-up stats ---------- */
  var counters = [].slice.call(doc.querySelectorAll('[data-count]'));
  if (counters.length && 'IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return; co.unobserve(en.target);
        var el = en.target, end = parseFloat(el.dataset.count), suf = el.dataset.suffix || '', t0 = null;
        if (reduce) { el.textContent = end + suf; return; }
        (function step(ts) {
          if (!t0) t0 = ts; var p = Math.min((ts - t0) / 1400, 1), e = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(end * e) + suf; if (p < 1) requestAnimationFrame(step);
        })(performance.now());
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  }

  /* ---------- time-saved estimator ---------- */
  var est = doc.querySelector('[data-estimator]');
  if (est) {
    var rs = est.querySelectorAll('input[type=range]');
    var outHrs = est.querySelector('[data-out-hours]'), outDays = est.querySelector('[data-out-days]');
    var update = function () {
      var team = +rs[0].value, hrs = +rs[1].value, share = +rs[2].value / 100;
      [].forEach.call(rs, function (r) {
        var p = (r.value - r.min) / (r.max - r.min) * 100; r.style.setProperty('--p', p + '%');
        r.parentNode.querySelector('output').textContent = r.dataset.fmt === 'pct' ? r.value + '%' : r.value;
      });
      var yearly = Math.round(team * hrs * share * 48); // 48 working weeks
      outHrs.textContent = yearly.toLocaleString('en-US');
      outDays.textContent = Math.round(yearly / 8).toLocaleString('en-US');
    };
    [].forEach.call(rs, function (r) { r.addEventListener('input', update); });
    update();
  }

  /* ---------- contact form (Web3Forms, same endpoint as the previous site) ---------- */
  var form = doc.getElementById('inquiryForm');
  if (form) {
    var status = doc.getElementById('formStatus');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('[name=botcheck]').value) return;
      var btn = form.querySelector('button[type=submit]');
      btn.disabled = true; status.textContent = 'Sending your message…';
      var fd = new FormData(form);
      fd.append('access_key', 'e3f091f5-4e4c-43c9-a18c-840be3a301cd');
      fd.append('subject', 'New Inquiry from ToolsRhino Website');
      fd.append('from_name', 'ToolsRhino Website');
      fetch('https://api.web3forms.com/submit', { method: 'POST', body: fd })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (d.success) { status.textContent = "Thank you. We've received your message and will reply within one business day."; form.reset(); }
          else throw new Error('fail');
        })
        .catch(function () { status.textContent = 'Something went wrong. Please email us directly at info@connectlyx.com.'; })
        .then(function () { btn.disabled = false; });
    });
  }

  var qi = (new URLSearchParams(location.search)).get('interest'), sel = doc.getElementById('s');
  if (qi && sel) { [].forEach.call(sel.options, function (o) { if (o.value === qi) sel.value = qi; }); }

  var y = doc.getElementById('year'); if (y) y.textContent = new Date().getFullYear();

  /* ---------- living ink (WebGL fluid background) ---------- */
  var VERT = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  var FRAG = [
    'precision highp float;',
    'uniform vec2 R;uniform float T;uniform vec2 M;uniform float E;',
    'float h(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}',
    'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);',
    ' return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}',
    'float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*n(p);p=p*2.03+vec2(1.7,9.2);a*=.5;}return v;}',
    'void main(){',
    ' float s=min(R.x,R.y);vec2 p=(gl_FragCoord.xy-.5*R)/s;vec2 m=(M-.5*R)/s;',
    ' float t=T*.055;float d=length(p-m);',
    ' vec2 push=(p-m)*exp(-d*3.2)*.5*E;',
    ' vec2 q=vec2(fbm(p*1.5+t),fbm(p*1.5+vec2(5.2,1.3)-t));',
    ' vec2 r=vec2(fbm(p*1.7+3.*q+vec2(1.7,9.2)+t*1.4+push*2.),fbm(p*1.7+3.*q+vec2(8.3,2.8)-t*1.1-push));',
    ' float f=fbm(p*1.4+3.4*r+push);',
    ' vec3 navy=vec3(.024,.051,.141);vec3 deep=vec3(.102,.173,.357);vec3 royal=vec3(0.,.278,.671);',
    ' vec3 ice=vec3(.686,.859,.961);vec3 blue=vec3(.12,.435,.88);',
    ' vec3 c=mix(navy,deep,smoothstep(.12,.55,f));',
    ' c=mix(c,royal,smoothstep(.38,.8,f*(.6+r.x)));',
    ' c=mix(c,blue,smoothstep(.45,.95,length(q)*f*1.7)*.8);',
    ' c=mix(c,ice,smoothstep(.5,.92,f*length(r)*1.5)*.95);',
    ' c+=vec3(.55,.75,1.)*exp(-d*5.)*.12*E;',
    ' float v=smoothstep(1.35,.2,length(p*vec2(.7,1.)));c*=.55+.45*v;',
    ' gl_FragColor=vec4(c,1.);}'
  ].join('\n');

  function Ink(canvas) {
    var gl = canvas.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'low-power' });
    if (!gl) return false;
    function sh(type, src) { var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return gl.getShaderParameter(s, gl.COMPILE_STATUS) ? s : null; }
    var vs = sh(gl.VERTEX_SHADER, VERT), fs = sh(gl.FRAGMENT_SHADER, FRAG); if (!vs || !fs) return false;
    var pr = gl.createProgram(); gl.attachShader(pr, vs); gl.attachShader(pr, fs); gl.linkProgram(pr);
    if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return false;
    gl.useProgram(pr);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    var loc = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    var uR = gl.getUniformLocation(pr, 'R'), uT = gl.getUniformLocation(pr, 'T'), uM = gl.getUniformLocation(pr, 'M'), uE = gl.getUniformLocation(pr, 'E');
    var scale = Math.min(window.devicePixelRatio || 1, 1) * 0.62, w = 0, h = 0;
    var mx = 0, my = 0, tx = 0, ty = 0, en = 0, ten = 0, visible = true, raf = 0, t0 = performance.now(), last = 0;
    var host = canvas.parentElement;
    function size() {
      var r = canvas.getBoundingClientRect(); w = Math.max(2, Math.round(r.width * scale)); h = Math.max(2, Math.round(r.height * scale));
      canvas.width = w; canvas.height = h; gl.viewport(0, 0, w, h); mx = tx = w * .6; my = ty = h * .55;
    }
    size(); window.addEventListener('resize', size);
    host.addEventListener('pointermove', function (e) {
      var r = canvas.getBoundingClientRect(); tx = (e.clientX - r.left) * (w / r.width); ty = (r.bottom - e.clientY) * (h / r.height); ten = 1;
    }, { passive: true });
    host.addEventListener('pointerleave', function () { ten = 0; });
    function frame(now) {
      raf = 0; if (!visible || doc.hidden) return;
      if (now - last < 33) { raf = requestAnimationFrame(frame); return; } last = now; // ~30fps is plenty for slow ink
      mx += (tx - mx) * .08; my += (ty - my) * .08; en += (ten - en) * .06;
      gl.uniform2f(uR, w, h); gl.uniform1f(uT, (now - t0) / 1000 + 20); gl.uniform2f(uM, mx, my); gl.uniform1f(uE, en);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      if (!reduce) raf = requestAnimationFrame(frame);
    }
    function kick() { if (!raf) raf = requestAnimationFrame(frame); }
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en2) { visible = en2[0].isIntersecting; if (visible) kick(); }).observe(canvas);
    doc.addEventListener('visibilitychange', kick);
    kick(); return true;
  }
  [].forEach.call(doc.querySelectorAll('canvas.ink'), function (c) { try { Ink(c); } catch (e) { /* CSS gradient fallback stays */ } });
})();
