(function () {
  var d = document;

  // Scroll-in animations: content is fully visible without JS; this only adds motion.
  var motion = !matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (motion && 'IntersectionObserver' in window) {
    d.documentElement.classList.add('anim');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in'); io.unobserve(e.target); count(e.target);
      });
    }, { threshold: .3 });
    d.querySelectorAll('[data-anim]').forEach(function (el) { io.observe(el); });
  }
  function count(root) {
    root.querySelectorAll('[data-count]').forEach(function (el) {
      var to = +el.dataset.count, pre = el.dataset.pre || '', suf = el.dataset.suf || '', t0;
      function f(t) {
        t0 = t0 || t; var p = Math.min((t - t0) / 1200, 1);
        el.textContent = pre + Math.round(to * (1 - Math.pow(1 - p, 3))) + suf;
        if (p < 1) requestAnimationFrame(f);
      }
      requestAnimationFrame(f);
    });
  }

  // Membership calculator: $89 per call vs $120/yr + $60 per call
  var r = d.getElementById('calls');
  if (r) {
    var $ = function (id) { return d.getElementById(id); }, v = $('c-v');
    var upd = function () {
      var n = +r.value, no = 89 * n, me = 120 + 60 * n, s = no - me;
      $('c-n').textContent = n; $('c-no').textContent = '$' + no; $('c-me').textContent = '$' + me;
      v.textContent = s > 0 ? v.dataset.save.replace('X', s) : v.dataset.nosave;
      v.classList.toggle('save', s > 0);
    };
    r.addEventListener('input', upd); upd();
  }

  // Reviews carousel: arrows only when there is more than one review
  var car = d.querySelector('.carousel'), nav = d.querySelector('.car-nav');
  if (car && nav && car.children.length > 1) {
    nav.classList.add('on');
    nav.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () { car.scrollBy({ left: car.clientWidth * +b.dataset.dir, behavior: 'smooth' }); });
    });
  }
})();
