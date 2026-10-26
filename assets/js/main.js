// Nav state, mobile menu, scroll reveal, count-up stats, hero chat demo, sticky CTA, click-to-play video.
(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const nav = document.querySelector(".nav");

  // nav border after scrolling + mobile menu
  const onScroll = () => nav && nav.classList.toggle("scrolled", window.scrollY > 8);
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  const menuBtn = document.querySelector(".menu-btn");
  if (menuBtn) {
    menuBtn.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open);
    });
    document.querySelectorAll(".nav-links a").forEach(a => a.addEventListener("click", () => {
      nav.classList.remove("open");
      menuBtn.setAttribute("aria-expanded", "false");
    }));
  }

  // count-up numbers: <span data-count="100" data-decimals="0">
  const countUp = el => {
    const end = parseFloat(el.dataset.count), dec = parseInt(el.dataset.decimals || "0", 10);
    if (reduce) { el.textContent = end.toFixed(dec); return; }
    const t0 = performance.now(), dur = 1400;
    const tick = now => {
      const p = Math.min((now - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (end * eased).toFixed(dec);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  // reveal on scroll
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      e.target.querySelectorAll("[data-count]").forEach(countUp);
      io.unobserve(e.target);
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
  document.querySelectorAll(".reveal, .steps").forEach(el => io.observe(el));

  // hero chat demo: question -> typing -> answer with source, looping through examples
  const chat = document.querySelector(".chat");
  if (chat) {
    const convo = [
      { q: "How many days of annual leave do full-time staff get?", a: "Full-time employees get 25 days of paid annual leave plus UK bank holidays.", src: "Northwind_Employee_Handbook.pdf · page 1" },
      { q: "Can I go diving with the TrailPro X2?", a: "No. It is water resistant to 50 metres and fine for swimming, but not for diving.", src: "TrailPro_X2_User_Manual.pdf · page 2" },
      { q: "Who is the CEO of the company?", a: "I don't have information about this in the documents.", src: "", refuse: true },
    ];
    const typing = chat.querySelector(".typing");
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    const add = (cls, html) => {
      const m = document.createElement("div");
      m.className = "msg " + cls;
      m.innerHTML = html;
      chat.insertBefore(m, typing);
      requestAnimationFrame(() => requestAnimationFrame(() => m.classList.add("show")));
      return m;
    };
    const run = async () => {
      if (reduce) {
        convo.slice(0, 2).forEach(c => { add("q show", c.q); add("a show", `${c.a}<span class="src">Source: ${c.src}</span>`); });
        return;
      }
      for (let round = 0; ; round++) {
        const c = convo[round % convo.length];
        chat.querySelectorAll(".msg").forEach(m => { m.classList.remove("show"); setTimeout(() => m.remove(), 450); });
        await sleep(600);
        add("q", c.q);
        await sleep(900);
        typing.classList.add("show");
        await sleep(1500);
        typing.classList.remove("show");
        add("a" + (c.refuse ? " refuse" : ""), c.a + (c.src ? `<span class="src">Source: ${c.src}</span>` : `<span class="src">Refused: not in your files</span>`));
        await sleep(4200);
      }
    };
    // start when visible
    const cio = new IntersectionObserver(es => { if (es[0].isIntersecting) { run(); cio.disconnect(); } });
    cio.observe(chat);
  }

  // sticky "Hire me" bar on phones once the hero is out of view
  const sticky = document.querySelector(".sticky-cta"), hero = document.querySelector(".hero, .cs-hero");
  if (sticky && hero) {
    new IntersectionObserver(es => sticky.classList.toggle("show", !es[0].isIntersecting)).observe(hero);
  }

  // video loads only when clicked
  document.querySelectorAll(".video[data-src]").forEach(box => {
    const start = () => {
      const v = document.createElement("video");
      v.src = box.dataset.src; v.controls = true; v.autoplay = true; v.playsInline = true;
      box.replaceChildren(v);
    };
    box.addEventListener("click", start, { once: true });
    box.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); start(); } }, { once: true });
  });

  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
