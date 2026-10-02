(() => {
  const header=document.querySelector('.site-header');
  const menu=document.querySelector('.menu-toggle');
  const nav=document.querySelector('.nav-links');
  const cursor=document.querySelector('.cursor-orb');
  const reveal=document.querySelectorAll('.reveal');
  const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const onScroll=()=>header?.classList.toggle('scrolled',window.scrollY>20);
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

  menu?.addEventListener('click',()=>{
    const open=nav.classList.toggle('open');
    menu.setAttribute('aria-expanded',open?'true':'false');
  });
  nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));

  if(cursor && !reduce){
    let tx=innerWidth/2,ty=innerHeight/2,x=tx,y=ty;
    window.addEventListener('pointermove',e=>{tx=e.clientX;ty=e.clientY},{passive:true});
    const loop=()=>{x+=(tx-x)*.08;y+=(ty-y)*.08;cursor.style.left=x+'px';cursor.style.top=y+'px';requestAnimationFrame(loop)};loop();
  }

  if('IntersectionObserver' in window){
    const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
    reveal.forEach(el=>io.observe(el));
  }else reveal.forEach(el=>el.classList.add('in'));

  if(!reduce){
    document.querySelectorAll('.tilt').forEach(card=>{
      card.addEventListener('pointermove',e=>{
        const r=card.getBoundingClientRect(),rx=((e.clientY-r.top)/r.height-.5)*-5,ry=((e.clientX-r.left)/r.width-.5)*5;
        card.style.transform=`perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-6px)`;
      });
      card.addEventListener('pointerleave',()=>card.style.transform='');
    });
  }
})();

/* =========================================================
   HOME PORTFOLIO — SCROLL REVEAL
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const portfolioCards = document.querySelectorAll(
        ".home-portfolio-card"
    );

    if (!portfolioCards.length) return;

    const observer = new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("portfolio-visible");

                    observer.unobserve(entry.target);

                }

            });

        },
        {
            threshold: 0.15
        }
    );

    portfolioCards.forEach((card, index) => {

        card.style.transitionDelay =
            `${index * 90}ms`;

        observer.observe(card);

    });

});


/* =========================================================
   PORTFOLIO — MOUSE 3D TILT
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(
        ".home-portfolio-card"
    );

    if (!cards.length) return;

    cards.forEach((card) => {

        card.addEventListener("mousemove", (e) => {

            const rect = card.getBoundingClientRect();

            const x =
                e.clientX - rect.left;

            const y =
                e.clientY - rect.top;

            const centerX =
                rect.width / 2;

            const centerY =
                rect.height / 2;

            const rotateY =
                ((x - centerX) / centerX) * 5;

            const rotateX =
                ((centerY - y) / centerY) * 5;

            card.style.transform =
                `perspective(900px)
                 rotateX(${rotateX}deg)
                 rotateY(${rotateY}deg)
                 translateY(-10px)
                 scale(1.015)`;

            /* Moving glow */

            card.style.setProperty(
                "--mouse-x",
                `${x}px`
            );

            card.style.setProperty(
                "--mouse-y",
                `${y}px`
            );

        });


        card.addEventListener("mouseleave", () => {

            card.style.transform = "";

        });

    });

});