import os
from datetime import datetime
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Begam Ji's Birthday", description="Luxury Romantic Experience")

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ========== CONFIGURATION — YAHAN APNI DETAILS BHARO ==========
CORRECT_PASSWORD = "HAPPY BIRTHDAY WIFFEEEYYY JIII"

RELATIONSHIP_START = datetime(2023, 1, 15, 18, 30)

PHOTO_CONFIG = [
    {"img": "photo1.jpg", "title": "Saari Mein",        "desc": "Sabse khoobsurat insaan is duniya mein 💘"},
    {"img": "photo2.jpg", "title": "Teri Aankhein",     "desc": "In aankhon mein doob jaata hoon har baar ✨"},
    {"img": "photo3.jpg", "title": "Woh Muskaan",       "desc": "Jab muskurati ho, toh dil tham jaata hai 💖"},
    {"img": "photo4.jpg", "title": "Tumhari Ada",       "desc": "Har ada pe dil fida — hamesha 💕"},
    {"img": "photo5.jpg", "title": "Meri Noor",         "desc": "Duniya ki sabse pyaari — meri rooshni 🌸"},
    {"img": "photo6.jpg", "title": "Meri Zindagi",      "desc": "Tum ho toh sab kuch hai — tum nahi toh kuch nahi 🌙"},
]

LOVE_LETTER = """Meri Jaan Begam Ji,

Tumhari har saans mein basi hai meri khushiyan,
Tumhari har muskaan meri duniya roshan kar deti hai.

Tum mere dil ki woh khoobsurat kahani ho,
Jise main har roz padhta hoon aur har baar naya lagta hai.

Tumhari aankhon mein maine apni jannat dekhi hai,
Tumhari bahon mein maine apni duniya payi hai.

Aaj tera birthday hai, lekin mujhe lagta hai jaise
Meri zindagi ka sabse haseen tohfa mujhe tu roz deti hai.

Ishq mein tumse behtar koi nahi —
Na tha, na hai, na hoga kabhi.

Dua hai meri Khuda se,
Tujhe hamesha khush rakhe, hamesha roshan rakhe.

Hamesha tumhara,
Mustafa ❤️"""

# =====================================================================
COMPLETE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Begam Ji — Ek Khaas Din</title>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Cinzel:wght@400;500;600&family=EB+Garamond:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
  <style>
    :root {
      --black:        #06030a;
      --velvet:       #0f0818;
      --velvet2:      #1a0e28;
      --velvet3:      #241535;
      --gold:         #c9a84c;
      --gold2:        #e8d08a;
      --gold3:        #f7eed4;
      --rose:         #b5294e;
      --rose2:        #d4567a;
      --rose3:        #f0a0bb;
      --rose4:        #fce8f0;
      --cream:        #f5edd8;
      --text:         #e8ddd0;
      --text2:        #a89580;
      --serif:        'Cormorant Garamond', Georgia, serif;
      --display:      'Cinzel', serif;
      --body:         'EB Garamond', Georgia, serif;
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--body);
      background: var(--black);
      color: var(--text);
      overflow-x: hidden;
      cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="%23c9a84c"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>') 11 11, auto;
    }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--velvet); }
    ::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 4px; }
    ::selection { background: var(--rose); color: #fff; }

    #bgCanvas { position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:0.5; }
    .petal { position:fixed;pointer-events:none;z-index:2;animation:petalFall linear forwards;opacity:0.6;font-size:1.1rem;filter:drop-shadow(0 0 6px rgba(201,168,76,0.5)); }
    @keyframes petalFall { 0%{transform:translateY(-5vh) translateX(0) rotate(0deg);opacity:0;}8%{opacity:0.7;}90%{opacity:0.4;}100%{transform:translateY(108vh) translateX(30px) rotate(400deg);opacity:0;} }
    .spark { position:fixed;pointer-events:none;z-index:9999;font-size:0.85rem;animation:sparkFly 0.9s ease-out forwards; }
    @keyframes sparkFly { 0%{opacity:1;transform:translate(0,0) scale(0.6);}100%{opacity:0;transform:translate(var(--dx),var(--dy)) scale(1.4);} }

    .reveal { opacity:0;transform:translateY(50px);transition:opacity 0.9s cubic-bezier(.16,1,.3,1),transform 0.9s cubic-bezier(.16,1,.3,1); }
    .reveal.visible { opacity:1;transform:translateY(0); }
    .reveal-left  { opacity:0;transform:translateX(-60px);transition:opacity 0.9s cubic-bezier(.16,1,.3,1),transform 0.9s cubic-bezier(.16,1,.3,1); }
    .reveal-right { opacity:0;transform:translateX(60px); transition:opacity 0.9s cubic-bezier(.16,1,.3,1),transform 0.9s cubic-bezier(.16,1,.3,1); }
    .reveal-left.visible,.reveal-right.visible { opacity:1;transform:translateX(0); }

    .gold-line { width:120px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:0 auto 2rem; }
    .gold-line-full { width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--gold) 30%,var(--gold) 70%,transparent);margin:3rem 0;opacity:0.4; }
    .section-wrap { position:relative;z-index:5;max-width:900px;margin:0 auto;padding:0 1.5rem; }
    .glass-card { background:rgba(26,14,40,0.75);backdrop-filter:blur(18px);border:1px solid rgba(201,168,76,0.18);border-radius:24px;padding:3rem 2.5rem;box-shadow:0 8px 60px rgba(0,0,0,0.6),inset 0 0 60px rgba(201,168,76,0.03); }
    @media(max-width:640px){ .glass-card{padding:2rem 1.25rem;} }

    /* HERO */
    #hero { position:relative;z-index:5;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:4rem 1.5rem;overflow:hidden; }
    #hero::before { content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 40%,rgba(181,41,78,0.18) 0%,rgba(201,168,76,0.06) 50%,transparent 100%);pointer-events:none; }
    .hero-ornament { font-family:var(--display);font-size:clamp(0.65rem,1.5vw,0.85rem);letter-spacing:0.4em;color:var(--gold);text-transform:uppercase;opacity:0.8;margin-bottom:1.5rem;animation:fadeSlideDown 1.4s cubic-bezier(.16,1,.3,1) both; }
    .hero-title { font-family:var(--display);font-size:clamp(2.4rem,8vw,6.5rem);font-weight:400;color:var(--cream);line-height:1.08;letter-spacing:0.04em;animation:fadeSlideDown 1.6s cubic-bezier(.16,1,.3,1) 0.15s both; }
    .hero-title span { display:block;background:linear-gradient(135deg,var(--gold),var(--gold2),var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text; }
    .hero-sub { font-family:var(--serif);font-style:italic;font-size:clamp(1.1rem,2.5vw,1.6rem);color:var(--rose3);margin-top:1.2rem;letter-spacing:0.05em;animation:fadeSlideDown 1.8s cubic-bezier(.16,1,.3,1) 0.3s both; }
    .hero-date { margin-top:2.5rem;font-family:var(--serif);font-size:1rem;color:var(--text2);letter-spacing:0.25em;text-transform:uppercase;animation:fadeSlideDown 2s cubic-bezier(.16,1,.3,1) 0.45s both; }
    .hero-ring { position:absolute;width:min(500px,90vw);height:min(500px,90vw);border-radius:50%;border:1px solid rgba(201,168,76,0.12);animation:ringPulse 5s ease-in-out infinite; }
    .hero-ring:nth-child(2){width:min(380px,70vw);height:min(380px,70vw);animation-delay:1.5s;}
    .hero-ring:nth-child(3){width:min(260px,55vw);height:min(260px,55vw);animation-delay:3s;border-color:rgba(181,41,78,0.15);}
    @keyframes ringPulse{0%,100%{opacity:0.3;transform:scale(1);}50%{opacity:0.7;transform:scale(1.04);}}
    .scroll-hint{position:absolute;bottom:2.5rem;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:6px;animation:fadeSlideDown 2.2s 1s both;cursor:default;}
    .scroll-hint span{font-family:var(--display);font-size:0.65rem;letter-spacing:0.35em;color:var(--text2);text-transform:uppercase;}
    .scroll-arrow{width:1px;height:50px;background:linear-gradient(to bottom,var(--gold),transparent);animation:arrowDrop 2s ease-in-out infinite;}
    @keyframes arrowDrop{0%,100%{transform:scaleY(1);opacity:0.6;}50%{transform:scaleY(1.2);opacity:1;}}
    @keyframes fadeSlideDown{from{opacity:0;transform:translateY(-25px);}to{opacity:1;transform:translateY(0);}}

    /* LETTER */
    #letter { padding:6rem 0; }
    .section-label { font-family:var(--display);font-size:0.7rem;letter-spacing:0.4em;color:var(--gold);text-transform:uppercase;text-align:center;margin-bottom:0.75rem;opacity:0.8; }
    .section-title { font-family:var(--serif);font-size:clamp(1.9rem,4vw,3rem);font-weight:300;text-align:center;color:var(--cream);line-height:1.2;margin-bottom:1.2rem; }
    .section-title em { color:var(--gold2);font-style:italic; }
    #letterText { font-family:var(--serif);font-size:clamp(1.05rem,2vw,1.3rem);line-height:2;color:var(--text);white-space:pre-wrap;min-height:200px;position:relative; }
    #letterText::after{content:'|';display:inline-block;color:var(--gold);animation:blink 0.8s step-end infinite;margin-left:2px;}
    #letterText.done::after{display:none;}
    @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
    .letter-sig { margin-top:2rem;text-align:right;font-family:var(--serif);font-style:italic;color:var(--gold2);font-size:1.15rem; }

    /* GALLERY */
    #gallery { padding:6rem 0; }
    .gallery-grid { display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:2rem;margin-top:3rem; }
    @media(max-width:500px){.gallery-grid{grid-template-columns:repeat(2,1fr);gap:1rem;}}
    .polaroid { background:#1c1225;border:1px solid rgba(201,168,76,0.15);padding:12px 12px 40px;cursor:pointer;transform:rotate(var(--r,0deg));transition:transform 0.45s cubic-bezier(.16,1,.3,1),box-shadow 0.45s ease,border-color 0.3s;box-shadow:0 6px 30px rgba(0,0,0,0.5); }
    .polaroid:hover{transform:rotate(0deg) scale(1.04) translateY(-8px)!important;box-shadow:0 25px 60px rgba(0,0,0,0.7),0 0 30px rgba(201,168,76,0.15);border-color:rgba(201,168,76,0.5);z-index:10;}
    .polaroid img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;filter:saturate(0.85) contrast(1.05);transition:filter 0.4s;}
    .polaroid:hover img{filter:saturate(1.1) contrast(1.05);}
    .polaroid-caption{text-align:center;padding-top:0.75rem;}
    .polaroid-caption strong{display:block;font-family:var(--display);font-size:0.7rem;letter-spacing:0.15em;color:var(--gold);text-transform:uppercase;margin-bottom:4px;}
    .polaroid-caption p{font-family:var(--serif);font-style:italic;font-size:0.85rem;color:var(--text2);line-height:1.4;}

    /* COUNTER */
    #counter { padding:6rem 0; }
    .counter-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.25rem;margin-top:3rem;}
    @media(max-width:560px){.counter-grid{grid-template-columns:repeat(2,1fr);}}
    .counter-box{background:rgba(15,8,24,0.7);border:1px solid rgba(201,168,76,0.2);border-radius:20px;padding:2rem 1rem;text-align:center;position:relative;overflow:hidden;transition:border-color 0.3s,box-shadow 0.3s;}
    .counter-box::before{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);opacity:0;transition:opacity 0.3s;}
    .counter-box:hover{border-color:rgba(201,168,76,0.5);box-shadow:0 0 30px rgba(201,168,76,0.1);}
    .counter-box:hover::before{opacity:1;}
    .counter-num{font-family:var(--display);font-size:clamp(2rem,5vw,3.2rem);font-weight:400;color:var(--gold);display:block;line-height:1;margin-bottom:0.6rem;}
    .counter-label{font-family:var(--display);font-size:0.6rem;letter-spacing:0.3em;color:var(--text2);text-transform:uppercase;}

    /* REASONS */
    #reasons { padding:6rem 0; }
    .reasons-track{display:flex;gap:1.25rem;overflow-x:auto;padding:1.5rem 0 2rem;scrollbar-width:none;-webkit-overflow-scrolling:touch;cursor:grab;}
    .reasons-track::-webkit-scrollbar{display:none;}
    .reasons-track:active{cursor:grabbing;}
    .reason-card{flex:0 0 240px;background:rgba(15,8,24,0.85);border:1px solid rgba(201,168,76,0.15);border-radius:20px;padding:2rem 1.5rem;text-align:center;transition:transform 0.35s,border-color 0.35s,box-shadow 0.35s;user-select:none;}
    .reason-card:hover{transform:translateY(-8px);border-color:rgba(201,168,76,0.45);box-shadow:0 20px 50px rgba(0,0,0,0.5),0 0 20px rgba(201,168,76,0.08);}
    .reason-icon{font-size:2.2rem;margin-bottom:1rem;display:block;filter:drop-shadow(0 0 10px rgba(201,168,76,0.4));}
    .reason-num{font-family:var(--display);font-size:0.6rem;letter-spacing:0.3em;color:var(--gold);text-transform:uppercase;margin-bottom:0.6rem;display:block;}
    .reason-text{font-family:var(--serif);font-size:1rem;font-style:italic;color:var(--text);line-height:1.6;}

    /* SHE WHY ME VIDEO */
    #sheWhyMeSection { padding:6rem 0; }
    .video-container {
      position:relative;
      width:100%;
      max-width:720px;
      margin:0 auto;
      border-radius:20px;
      overflow:hidden;
      border:1px solid rgba(201,168,76,0.25);
      box-shadow:0 20px 80px rgba(0,0,0,0.7), 0 0 40px rgba(181,41,78,0.1);
    }
    .video-container video {
      width:100%; display:block;
      background:#000;
    }
    .video-fallback {
      padding:4rem 2rem;
      text-align:center;
      background:rgba(15,8,24,0.9);
    }
    .video-fallback p { font-family:var(--serif);font-style:italic;color:var(--text2);font-size:1rem; }
    .she-header {
      text-align:center;
      margin-bottom:2rem;
    }
    .she-question {
      font-family:'Cinzel',serif;
      font-size:clamp(1.8rem,5vw,3.2rem);
      font-weight:400;
      letter-spacing:0.06em;
      background:linear-gradient(135deg,#f5edd8 30%,#c9a84c 60%,#f0a0bb 100%);
      -webkit-background-clip:text;
      -webkit-text-fill-color:transparent;
      background-clip:text;
      margin-bottom:0.5rem;
    }
    .she-sub {
      font-family:var(--serif);
      font-style:italic;
      color:var(--rose3);
      font-size:1rem;
      opacity:0.8;
    }
    @keyframes shimmerText {
      0%   { background-position:0% 50%; }
      100% { background-position:100% 50%; }
    }

    /* SURPRISES */
    #surprises { padding:6rem 0; }
    .flip-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1.25rem;margin-top:3rem;}
    .flip-wrap{perspective:800px;height:170px;cursor:pointer;}
    .flip-inner{position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform 0.7s cubic-bezier(.16,1,.3,1);}
    .flip-wrap.flipped .flip-inner{transform:rotateY(180deg);}
    .flip-face{position:absolute;inset:0;backface-visibility:hidden;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:1.2rem;}
    .flip-front{background:linear-gradient(145deg,var(--velvet2),var(--velvet3));border:1px solid rgba(201,168,76,0.25);box-shadow:0 6px 30px rgba(0,0,0,0.4);}
    .flip-back{transform:rotateY(180deg);background:linear-gradient(145deg,#1e0f30,#2a1045);border:1px solid rgba(181,41,78,0.35);box-shadow:0 6px 30px rgba(0,0,0,0.4);}
    .flip-icon{font-size:2rem;margin-bottom:0.6rem;filter:drop-shadow(0 0 8px rgba(201,168,76,0.5));}
    .flip-label{font-family:var(--display);font-size:0.65rem;letter-spacing:0.2em;color:var(--gold);text-transform:uppercase;}
    .flip-hint{font-size:0.65rem;color:var(--text2);margin-top:6px;font-family:var(--serif);font-style:italic;}
    .flip-msg{font-family:var(--serif);font-style:italic;font-size:0.88rem;color:var(--rose4);line-height:1.55;}

    /* GIFT */
    #gift { padding:6rem 0; }
    .gift-scene{display:flex;justify-content:center;align-items:center;padding:3rem 0;}
    .gift-wrap{position:relative;width:180px;height:180px;cursor:pointer;transform-style:preserve-3d;}
    .gift-wrap:hover{animation:giftShake 0.5s ease-in-out infinite;}
    @keyframes giftShake{0%,100%{transform:rotate(0deg);}25%{transform:rotate(-3deg) translateY(-4px);}75%{transform:rotate(3deg) translateY(-4px);}}
    .gift-body{position:absolute;bottom:0;left:0;right:0;height:115px;background:linear-gradient(145deg,#7a1530,#b5294e);border-radius:0 0 18px 18px;box-shadow:0 12px 40px rgba(181,41,78,0.4);}
    .gift-ribbon-v{position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:28px;height:115px;background:linear-gradient(180deg,var(--gold),var(--gold2));}
    .gift-ribbon-h{position:absolute;top:50px;left:0;right:0;height:28px;background:linear-gradient(90deg,var(--gold),var(--gold2),var(--gold));}
    .gift-lid{position:absolute;top:-18px;left:-6px;right:-6px;height:50px;background:linear-gradient(145deg,#9a1c3a,#c9335c);border-radius:10px;box-shadow:0 6px 20px rgba(0,0,0,0.4);transition:transform 0.7s cubic-bezier(.16,1,.3,1);transform-origin:bottom center;z-index:2;}
    .gift-lid-ribbon{position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:28px;height:100%;background:linear-gradient(180deg,var(--gold2),var(--gold));}
    .gift-bow{position:absolute;bottom:100%;left:50%;transform:translateX(-50%);display:flex;gap:4px;z-index:3;}
    .bow-loop{width:36px;height:26px;background:var(--gold);border-radius:50% 50% 0 0;box-shadow:0 4px 12px rgba(0,0,0,0.3);}
    .bow-loop:first-child{transform:rotate(-20deg) translateX(4px);}
    .bow-loop:last-child{transform:rotate(20deg) translateX(-4px);}
    .gift-wrap.opened .gift-lid{transform:rotate(-80deg) translateY(-20px);}
    .gift-glow{position:absolute;inset:-20px;background:radial-gradient(circle,rgba(201,168,76,0.15),transparent 70%);border-radius:50%;opacity:0;transition:opacity 0.5s;pointer-events:none;}
    .gift-wrap.opened .gift-glow{opacity:1;animation:glowPulse 2s ease-in-out infinite;}
    @keyframes glowPulse{0%,100%{opacity:0.5;}50%{opacity:1;}}

    /* CAKE */
    #cake { padding:6rem 0; }
    .cake-scene{display:flex;flex-direction:column;align-items:center;gap:1.5rem;}
    #cakeCanvas{border-radius:16px;max-width:100%;}
    #cakeInstruction{font-family:var(--serif);font-style:italic;color:var(--gold2);font-size:1rem;text-align:center;}
    #cakeMsg{display:none;font-family:var(--display);letter-spacing:0.15em;text-align:center;color:var(--gold);font-size:1.1rem;animation:bounceIn 0.6s ease;}
    @keyframes bounceIn{0%{transform:scale(0.5);opacity:0;}70%{transform:scale(1.08);}100%{transform:scale(1);opacity:1;}}

    /* WISHES */
    #wishes { padding:6rem 0; }
    .stars-row{display:flex;justify-content:center;flex-wrap:wrap;gap:2rem;margin-top:3rem;}
    .wish-star{font-size:2.8rem;cursor:pointer;filter:drop-shadow(0 0 8px rgba(201,168,76,0.3));transition:transform 0.25s,filter 0.25s;animation:starTwinkle var(--d,2s) ease-in-out infinite alternate;}
    @keyframes starTwinkle{from{opacity:0.6;transform:scale(1)}to{opacity:1;transform:scale(1.15)}}
    .wish-star:hover{transform:scale(1.4);filter:drop-shadow(0 0 20px rgba(201,168,76,0.9));}
    .wish-star.granted{animation:starBurst 0.5s ease;}
    @keyframes starBurst{0%{transform:scale(1)}50%{transform:scale(1.8)}100%{transform:scale(1.2)}}
    #wishGranted{display:none;margin-top:2rem;padding:2rem;background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-radius:20px;text-align:center;}
    #wishTitle{font-family:var(--display);font-size:0.75rem;letter-spacing:0.3em;color:var(--gold);text-transform:uppercase;margin-bottom:0.75rem;}
    #wishMsg{font-family:var(--serif);font-style:italic;font-size:1.2rem;color:var(--text);line-height:1.7;}

    /* LOVE PULSE */
    #lovePulse { padding:4rem 0; }
    @keyframes heartbeatBig{0%,100%{transform:scale(1);}14%{transform:scale(1.22);}28%{transform:scale(1);}42%{transform:scale(1.15);}56%{transform:scale(1);}}

    /* TICKER */
    #quoteTicker { padding:2rem 0;overflow:hidden; }
    @keyframes tickerScroll{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
    .ticker-item{display:inline-flex;align-items:center;gap:0.8rem;font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;color:var(--gold2);letter-spacing:0.04em;flex-shrink:0;}
    .ticker-sep{color:var(--rose);font-size:0.7rem;}

    /* MODAL */
    #modal{position:fixed;inset:0;background:rgba(0,0,0,0.82);backdrop-filter:blur(14px);z-index:8000;display:flex;align-items:center;justify-content:center;padding:1.5rem;opacity:0;visibility:hidden;transition:opacity 0.35s,visibility 0.35s;}
    #modal.active{opacity:1;visibility:visible;}
    .modal-inner{background:var(--velvet2);border:1px solid rgba(201,168,76,0.25);border-radius:28px;max-width:440px;width:100%;padding:2.5rem 2rem;text-align:center;box-shadow:0 40px 80px rgba(0,0,0,0.7),0 0 40px rgba(201,168,76,0.08);transform:scale(0.88) translateY(20px);transition:transform 0.45s cubic-bezier(.16,1,.3,1);}
    #modal.active .modal-inner{transform:scale(1) translateY(0);}
    .modal-img{width:100%;border-radius:16px;margin-bottom:1.25rem;max-height:250px;object-fit:cover;}
    .modal-title{font-family:var(--display);font-size:0.85rem;letter-spacing:0.2em;color:var(--gold);text-transform:uppercase;margin-bottom:0.6rem;}
    .modal-desc{font-family:var(--serif);font-style:italic;color:var(--text);font-size:1.05rem;line-height:1.7;}
    .modal-close{margin-top:1.5rem;padding:0.75rem 2.5rem;border-radius:50px;background:linear-gradient(135deg,var(--rose),var(--rose2));color:#fff;font-family:var(--display);font-size:0.7rem;letter-spacing:0.2em;text-transform:uppercase;border:none;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;}
    .modal-close:hover{transform:scale(1.04);box-shadow:0 8px 25px rgba(181,41,78,0.4);}

    /* FIREWORKS */
    #fwCanvas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:7000;display:none;}

    /* HEARTS RAIN */
    #heartsCanvas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:1;opacity:0;transition:opacity 1s;}

    /* FOOTER */
    footer{position:relative;z-index:5;text-align:center;padding:5rem 1.5rem 4rem;border-top:1px solid rgba(201,168,76,0.1);}
    .footer-quote{font-family:var(--serif);font-style:italic;font-size:clamp(1.1rem,2.5vw,1.5rem);color:var(--text);max-width:600px;margin:0 auto 2rem;line-height:1.8;}
    .footer-credit{font-family:var(--display);font-size:0.6rem;letter-spacing:0.3em;color:var(--text2);text-transform:uppercase;}

    .text-center{text-align:center;}
    .mt1{margin-top:1rem;}.mt2{margin-top:2rem;}.mt3{margin-top:3rem;}
  </style>
</head>
<body>

<canvas id="bgCanvas"></canvas>
<canvas id="fwCanvas"></canvas>
<div id="petalLayer"></div>

<!-- HERO -->
<section id="hero">
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <p class="hero-ornament">— A Birthday Dedication —</p>
  <h1 class="hero-title">Happy Birthday<span>Begam Ji</span></h1>
  <p class="hero-sub">Meri rooshni. Meri duniya. Meri sab kuch.</p>
  <p class="hero-date" id="heroDate">From Mustafa, with endless love</p>
  <div class="scroll-hint" aria-hidden="true">
    <span>Scroll</span>
    <div class="scroll-arrow"></div>
  </div>
</section>

<!-- LOVE LETTER -->
<section id="letter">
  <div class="section-wrap">
    <div class="reveal">
      <p class="section-label">A Letter From The Heart</p>
      <h2 class="section-title">Ek <em>Khaas Khat</em> Tumhare Naam</h2>
      <div class="gold-line"></div>
    </div>
    <div class="glass-card reveal" style="transition-delay:0.15s">
      <div id="letterText"></div>
      <div class="letter-sig">— Hamesha Tumhara, Mustafa ❤️</div>
    </div>
  </div>
</section>

<!-- GALLERY -->
<section id="gallery">
  <div class="section-wrap">
    <div class="reveal">
      <p class="section-label">BELLOW IS</p>
      <h2 class="section-title">MY MOST FAVORITE <em>GALLERY</em></h2>
      <div class="gold-line"></div>
      <p class="text-center" style="font-family:var(--serif);font-style:italic;color:var(--text2);margin-bottom:0.5rem">Har tasveer mein ek kahani hai — click karo aur mehsoos karo 🖤</p>
    </div>
    <div class="gallery-grid" id="galleryGrid"></div>
  </div>
</section>

<!-- TIME COUNTER -->
<section id="counter">
  <div class="section-wrap">
    <div class="reveal">
      <p class="section-label">Together Since</p>
      <h2 class="section-title">Hum <em>Saath Hain</em></h2>
      <div class="gold-line"></div>
    </div>
    <div class="counter-grid reveal" style="transition-delay:0.12s">
      <div class="counter-box"><span class="counter-num" id="cntYears">0</span><span class="counter-label">Saal</span></div>
      <div class="counter-box"><span class="counter-num" id="cntDays">0</span><span class="counter-label">Din</span></div>
      <div class="counter-box"><span class="counter-num" id="cntHours">0</span><span class="counter-label">Ghante</span></div>
      <div class="counter-box"><span class="counter-num" id="cntMins">0</span><span class="counter-label">Minute</span></div>
    </div>
  </div>
</section>

<!-- REASONS -->
<section id="reasons">
  <div class="section-wrap">
    <div class="reveal">
      <p class="section-label">From My Soul</p>
      <h2 class="section-title">Main Tumse <em>Kyun Pyaar Karta Hoon</em></h2>
      <div class="gold-line"></div>
      <p class="text-center" style="font-family:var(--serif);font-style:italic;color:var(--text2);margin-bottom:0">Swipe karo — har wajah dil se hai 🤍</p>
    </div>
    <div class="reasons-track" id="reasonsTrack"></div>
  </div>
</section>

<!-- SHE: WHY ME — VIDEO SECTION -->
<section id="sheWhyMeSection">
  <div class="section-wrap">
    <div class="reveal she-header">
      <p class="section-label">Ek Sawaal — Dil Se</p>
      <div class="she-question">She: Why Me?</div>
      <p class="she-sub">Yeh jawab sirf dil jaanta hai 💕</p>
      <div class="gold-line" style="margin-top:1.5rem"></div>
    </div>
    <div class="reveal" style="transition-delay:0.15s">
      <div class="video-container">
        <!-- VIDEO FILE: /static/jhol.mp4 — apni video is naam se static folder mein daalo -->
        <video
          id="jholVideo"
          controls
          preload="metadata"
          playsinline
          style="width:100%;display:block;background:#000;max-height:480px;object-fit:contain;"
          onerror="document.getElementById('videoFallback').style.display='block';this.style.display='none';"
        >
          <source src="/static/jhol.mp4" type="video/mp4">
          <source src="/static/jhol.webm" type="video/webm">
        </video>
        <div id="videoFallback" class="video-fallback" style="display:none;">
          <p style="font-size:2rem;margin-bottom:1rem">🎬</p>
          <p>Video file nahi mili — <code style="color:var(--gold);font-size:0.85rem">static/jhol.mp4</code> yahan daalo</p>
        </div>
      </div>
      <p style="text-align:center;font-family:var(--serif);font-style:italic;color:var(--text2);font-size:0.9rem;margin-top:1rem;opacity:0.7;">
        Here Is The Answer: <code style="color:var(--gold)">static/jhol.mp4</code> 
      </p>
    </div>
  </div>
</section>

<!-- LOVE PULSE METER -->
<section id="lovePulse" style="padding:4rem 0;">
  <div class="section-wrap text-center">
    <div class="reveal">
      <p class="section-label">My Heart Says</p>
      <h2 class="section-title">Dil Ki <em>Dhadkan</em></h2>
      <div class="gold-line"></div>
    </div>
    <div class="reveal glass-card" style="transition-delay:0.1s;padding:3rem 2rem;">
      <p style="font-family:var(--serif);font-style:italic;color:var(--text2);margin-bottom:2rem;">Yeh meter tab barhta hai jab Begam Ji paas hoti hain 💗</p>
      <div style="position:relative;height:18px;background:rgba(255,255,255,0.05);border-radius:50px;border:1px solid rgba(201,168,76,0.2);overflow:hidden;margin-bottom:1.5rem;">
        <div id="loveMeterBar" style="height:100%;width:0%;background:linear-gradient(90deg,#7a1530,#b5294e,#d4567a,#f0a0bb);border-radius:50px;transition:width 0.08s linear;box-shadow:0 0 20px rgba(181,41,78,0.5);"></div>
      </div>
      <div id="loveMeterLabel" style="font-family:var(--display);font-size:0.8rem;letter-spacing:0.3em;color:var(--gold);text-transform:uppercase;">Calculating love…</div>
      <div id="bigHeart" style="font-size:4rem;margin-top:1.5rem;display:inline-block;animation:heartbeatBig 1.4s ease-in-out infinite;filter:drop-shadow(0 0 20px rgba(181,41,78,0.6));cursor:pointer;" onclick="boostHeart()">❤️</div>
    </div>
  </div>
</section>

<!-- LOVE QUOTE TICKER -->
<section id="quoteTicker" style="padding:2rem 0;overflow:hidden;">
  <div style="border-top:1px solid rgba(201,168,76,0.12);border-bottom:1px solid rgba(201,168,76,0.12);background:rgba(10,3,20,0.6);padding:1.1rem 0;overflow:hidden;position:relative;z-index:5;">
    <div id="tickerTrack" style="display:flex;gap:4rem;white-space:nowrap;animation:tickerScroll 35s linear infinite;width:max-content;"></div>
  </div>
</section>

<!-- HEARTS RAIN TOGGLE -->
<canvas id="heartsCanvas"></canvas>
<button id="heartsToggle" onclick="toggleHearts()" style="position:fixed;bottom:1.5rem;right:1.25rem;width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#4a0f20,#7a1530);border:1px solid rgba(181,41,78,0.35);color:var(--rose3);font-size:1.1rem;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:9000;box-shadow:0 4px 20px rgba(181,41,78,0.25);transition:transform 0.2s,box-shadow 0.2s;" title="Toggle heart rain">🌸</button>

<!-- SURPRISE FLIP CARDS -->
<section id="surprises">
  <div class="section-wrap">
    <div class="reveal">
      <p class="section-label">Sealed With Love</p>
      <h2 class="section-title">Kuch <em>Khaas Surprises</em></h2>
      <div class="gold-line"></div>
      <p class="text-center" style="font-family:var(--serif);font-style:italic;color:var(--text2)">Har card ke andar ek raaz — click karo aur kholke dekho 🎴</p>
    </div>
    <div class="flip-grid" id="flipGrid"></div>
  </div>
</section>

<!-- VIRTUAL GIFT -->
<section id="gift">
  <div class="section-wrap text-center">
    <div class="reveal">
      <p class="section-label">For You</p>
      <h2 class="section-title">Mera <em>Khaas Tohfa</em></h2>
      <div class="gold-line"></div>
      <p style="font-family:var(--serif);font-style:italic;color:var(--text2);margin-bottom:0.5rem">Gift box pe click karo 🎁</p>
    </div>
    <div class="gift-scene reveal" style="transition-delay:0.1s">
      <div class="gift-wrap" id="giftWrap">
        <div class="gift-body"><div class="gift-ribbon-v"></div><div class="gift-ribbon-h"></div></div>
        <div class="gift-lid"><div class="gift-lid-ribbon"></div></div>
        <div class="gift-bow"><div class="bow-loop"></div><div class="bow-loop"></div></div>
        <div class="gift-glow"></div>
      </div>
    </div>
  </div>
</section>

<!-- BIRTHDAY CAKE -->
<section id="cake">
  <div class="section-wrap text-center">
    <div class="reveal">
      <p class="section-label">Make A Wish</p>
      <h2 class="section-title">Apna <em>Birthday Cake</em></h2>
      <div class="gold-line"></div>
    </div>
    <div class="cake-scene reveal" style="transition-delay:0.1s">
      <div id="cakeInstruction">🕯️ Candles pe click karke phoonk maro!</div>
      <canvas id="cakeCanvas" width="300" height="320"></canvas>
      <div id="cakeMsg">✦ Happy Birthday Begam Ji ✦<br><span style="font-size:0.9rem;color:var(--rose3);font-family:var(--serif);font-style:italic">May all your dreams bloom like roses 🌹</span></div>
    </div>
  </div>
</section>

<!-- WISHING STARS -->
<section id="wishes">
  <div class="section-wrap text-center">
    <div class="reveal">
      <p class="section-label">Wish Upon A Star</p>
      <h2 class="section-title">Ek <em>Dua Maango</em></h2>
      <div class="gold-line"></div>
      <p style="font-family:var(--serif);font-style:italic;color:var(--text2)">Kisi bhi star pe click karo💫</p>
    </div>
    <div class="stars-row" id="starsRow"></div>
    <div id="wishGranted" class="reveal">
      <div id="wishTitle">✦ Teri Dua Qabool Hui ✦</div>
      <div id="wishMsg"></div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="gold-line-full" style="margin-bottom:3rem"></div>
  <p class="footer-quote">"Tum ho toh main hoon —<br>Tum nahi toh main kuch nahi."</p>
  <div class="gold-line" style="margin-bottom:1.5rem"></div>
  <p class="footer-credit">Made with love by Mustafa — Sirf Begam Ji Ke Liye</p>
</footer>

<!-- MODAL -->
<div id="modal" role="dialog" aria-modal="true">
  <div class="modal-inner" id="modalInner">
    <div id="modalContent"></div>
  </div>
</div>

<script>
"use strict";

const START_DATE  = new Date({{ start_year }}, {{ start_month }}, {{ start_day }}, {{ start_hour }}, {{ start_minute }});
const PHOTOS      = {{ photos_json }};
const LOVE_LETTER = {{ love_letter_json }};

const REASONS = [
  { icon:"🌙", text:"Raat ko jab sote ho, tab bhi muskurate hue lagte ho — main tum par fida hoon." },
  { icon:"👁️", text:"Teri aankhein — inme doob jaata hoon, bahar aana hi nahi chahta." },
  { icon:"🌹", text:"Teri aadat — ek ek cheez jo tum karte ho, woh mujhe aur zyada pyaar karne par majboor karti hai." },
  { icon:"☀️", text:"Subah teri awaaz — mera sabse pyaara alarm hai, jo main kabhi band nahi karna chahta." },
  { icon:"🤝", text:"Har mushkil mein tum mera saath nahi chhodte — yeh sab se badi mohabbat hai." },
  { icon:"💬", text:"Teri baatein — ghante baat karein aur phir bhi mann nahi bharta." },
  { icon:"🍽️", text:"Tumhara pyaar se khana banana — har niwale mein mohabbat ka swad aata hai." },
  { icon:"🌸", text:"Teri muskaan — sab kuch theek ho jaata hai jab tum muskurate ho." },
  { icon:"🌙", text:"Tum mujhe behtar insaan banate ho — har roz thoda aur accha." },
  { icon:"💫", text:"Tum sirf meri Begam Ji nahi — tum meri poori duniya ho." },
];

const SURPRISES = [
  { icon:"💌", label:"Ek Raaz",      msg:"Tum meri zindagi ki sabse khoobsurat cheez ho — aur har subah tumhare baare mein sochke smile aati hai." },
  { icon:"🌹", label:"Wada",         msg:"Main hamesha tumhara haath thaamunga — har mushkil mein, har khushi mein, hamesha." },
  { icon:"🌙", label:"Raat Ki Baat", msg:"Jab bhi neend nahi aati, sirf teri yaad aati hai — aur lagta hai duniya khoobsurat hai." },
  { icon:"💫", label:"Meri Dua",     msg:"Allah se bas ek dua hai — Begam Ji ki muskaan hamesha bani rahe." },
  { icon:"🎁", label:"Asli Tohfa",   msg:"Tera sabse bada gift yeh hai ke tu meri hai — aur main sirf tera." },
  { icon:"🤗", label:"Hug Voucher",  msg:'"Unlimited Hugs Voucher" — Valid for lifetime. No expiry. Redeem anytime, any number of times.' },
  { icon:"🍰", label:"Meethi Baat",  msg:"Tum mere birthday cake se bhi zyada meethi ho — seriously, koi muqabla nahi." },
  { icon:"👑", label:"Meri Malika",  msg:"Tum sirf meri Begam Ji nahi — tum meri queen ho, meri duniya ho, mera sab kuch ho." },
];

const WISHES = [
  "Main tumhare har sapne poore karunga — har ek 💫",
  "Tumhari har khushi meri zimmedaari hai — hamesha ⭐",
  "Hum hamesha saath rahenge — is janam bhi, agle janam bhi 🌙",
  "Tera birthday sabse khaas hai mere liye — sirf tera 🎂",
  "Duniya ki sabse pyaari ho tum — koi shak nahi 🌹",
  "Har dua mein pehle tumhara naam aata hai — khuda gawah 💖",
];

/* STAR-DUST BG */
(function(){
  const c=document.getElementById('bgCanvas'),ctx=c.getContext('2d');
  let W,H,stars=[];
  function resize(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}
  window.addEventListener('resize',resize);resize();
  for(let i=0;i<220;i++) stars.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.2+0.2,a:Math.random(),s:(Math.random()-0.5)*0.003,vx:(Math.random()-0.5)*0.08,vy:(Math.random()-0.5)*0.08});
  function draw(){
    ctx.clearRect(0,0,W,H);
    stars.forEach(s=>{s.a+=s.s;if(s.a<0||s.a>1)s.s*=-1;s.x+=s.vx;s.y+=s.vy;if(s.x<0)s.x=W;if(s.x>W)s.x=0;if(s.y<0)s.y=H;if(s.y>H)s.y=0;ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fillStyle=`rgba(201,168,76,${s.a*0.7})`;ctx.fill();});
    requestAnimationFrame(draw);
  }
  draw();
})();

/* FALLING PETALS */
const PETAL_CHARS=['🌹','🌸','✦','❧','🥀'];
function spawnPetal(){
  const el=document.createElement('div');el.className='petal';
  el.textContent=PETAL_CHARS[Math.floor(Math.random()*PETAL_CHARS.length)];
  el.style.left=Math.random()*100+'vw';
  el.style.animationDuration=(6+Math.random()*8)+'s';
  el.style.fontSize=(0.7+Math.random()*0.8)+'rem';
  document.getElementById('petalLayer').appendChild(el);
  setTimeout(()=>el.remove(),14000);
}
setInterval(spawnPetal,900);

/* CURSOR SPARKLE */
const SPARKS=['✦','✧','·','*','◦'];
let lastSpark=0;
document.addEventListener('mousemove',e=>{
  const now=Date.now();if(now-lastSpark<80)return;lastSpark=now;
  const el=document.createElement('div');el.className='spark';
  el.textContent=SPARKS[Math.floor(Math.random()*SPARKS.length)];
  el.style.left=e.clientX+'px';el.style.top=e.clientY+'px';
  el.style.color=Math.random()>0.5?'#c9a84c':'#d4567a';
  el.style.setProperty('--dx',(Math.random()*40-20)+'px');
  el.style.setProperty('--dy',-(Math.random()*40+20)+'px');
  document.body.appendChild(el);setTimeout(()=>el.remove(),900);
});

/* SCROLL REVEAL */
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');});},{threshold:0.12});
document.querySelectorAll('.reveal,.reveal-left,.reveal-right').forEach(el=>observer.observe(el));

/* TIME COUNTER */
function updateCounter(){
  const diff=Date.now()-START_DATE.getTime();
  const totalDays=Math.floor(diff/86400000);
  const years=Math.floor(totalDays/365);
  const days=totalDays-years*365;
  const hours=Math.floor((diff%86400000)/3600000);
  const mins=Math.floor((diff%3600000)/60000);
  const set=(id,v)=>{const el=document.getElementById(id);if(el&&el.textContent!==String(v)){el.style.transform='translateY(-6px)';el.style.opacity='0';setTimeout(()=>{el.textContent=v;el.style.transition='transform 0.4s,opacity 0.4s';el.style.transform='translateY(0)';el.style.opacity='1';},200);}};
  set('cntYears',years);set('cntDays',days);set('cntHours',hours);set('cntMins',mins);
}
updateCounter();setInterval(updateCounter,30000);

/* TYPEWRITER LETTER */
const TW_EL=document.getElementById('letterText');
let twIdx=0;
function typeNext(){
  if(twIdx<=LOVE_LETTER.length){TW_EL.textContent=LOVE_LETTER.slice(0,twIdx);twIdx++;setTimeout(typeNext,38);}
  else TW_EL.classList.add('done');
}
const letterObs=new IntersectionObserver(entries=>{if(entries[0].isIntersecting&&twIdx===0){twIdx=1;typeNext();}},{threshold:0.2});
letterObs.observe(document.getElementById('letter'));

/* GALLERY */
const grid=document.getElementById('galleryGrid');
PHOTOS.forEach((p,i)=>{
  const rot=(Math.random()*4-2).toFixed(1);
  const card=document.createElement('div');card.className='polaroid reveal';
  card.style.cssText=`--r:${rot}deg;transition-delay:${i*0.08}s`;
  card.innerHTML=`<img src="/static/${p.img}" alt="${p.title}" onerror="this.src='https://placehold.co/400x300/1a0e28/c9a84c?text=♥'"><div class="polaroid-caption"><strong>${p.title}</strong><p>${p.desc}</p></div>`;
  card.addEventListener('click',()=>openModal(`<img class="modal-img" src="/static/${p.img}" onerror="this.src='https://placehold.co/440x280/1a0e28/c9a84c?text=♥'"><div class="modal-title">${p.title}</div><div class="modal-desc">${p.desc}</div><button class="modal-close" onclick="closeModal()">Close</button>`));
  grid.appendChild(card);observer.observe(card);
});

/* REASONS */
const track=document.getElementById('reasonsTrack');
REASONS.forEach((r,i)=>{
  const card=document.createElement('div');card.className='reason-card';
  card.innerHTML=`<span class="reason-icon">${r.icon}</span><span class="reason-num">Reason ${String(i+1).padStart(2,'0')}</span><p class="reason-text">${r.text}</p>`;
  track.appendChild(card);
});
let isDragging=false,startX,scrollLeft;
track.addEventListener('mousedown',e=>{isDragging=true;startX=e.pageX-track.offsetLeft;scrollLeft=track.scrollLeft;track.style.cursor='grabbing';});
track.addEventListener('mouseleave',()=>{isDragging=false;track.style.cursor='grab';});
track.addEventListener('mouseup',()=>{isDragging=false;track.style.cursor='grab';});
track.addEventListener('mousemove',e=>{if(!isDragging)return;e.preventDefault();const x=e.pageX-track.offsetLeft;track.scrollLeft=scrollLeft-(x-startX)*1.3;});

/* FLIP CARDS */
const flipGrid=document.getElementById('flipGrid');
SURPRISES.forEach((s,i)=>{
  const wrap=document.createElement('div');wrap.className='flip-wrap reveal';wrap.style.transitionDelay=(i*0.07)+'s';
  wrap.innerHTML=`<div class="flip-inner"><div class="flip-face flip-front"><div class="flip-icon">${s.icon}</div><div class="flip-label">${s.label}</div><div class="flip-hint">tap to reveal</div></div><div class="flip-face flip-back"><p class="flip-msg">${s.msg}</p></div></div>`;
  wrap.addEventListener('click',()=>{wrap.classList.toggle('flipped');if(wrap.classList.contains('flipped'))launchFireworks();});
  flipGrid.appendChild(wrap);observer.observe(wrap);
});

/* GIFT BOX */
const giftWrap=document.getElementById('giftWrap');
let giftOpened=false;
giftWrap.addEventListener('click',()=>{
  if(giftOpened)return;giftOpened=true;giftWrap.classList.add('opened');launchFireworks();
  setTimeout(()=>openModal(`<div style="font-size:3rem;margin-bottom:1rem">🎁</div><div class="modal-title">Meri Jaan — Ye Tohfa Tumhare Liye</div><div class="modal-desc" style="margin-top:1rem"><strong style="color:var(--gold2);display:block;margin-bottom:0.6rem">"Good for 1000 Hugs + Unlimited Pyaar"</strong>Har baar gale lagana mera haq hai — aur main hamesha tumhe yaad dilata rahunga ke main tumse kitna pyaar karta hoon.<br><br><span style="color:var(--rose3)">✦ Redeem Code: MUSTAFA_LOVES_BEGAMJI_FOREVER ✦</span></div><button class="modal-close" onclick="closeModal()">Accept With Love</button>`),500);
});

/* BIRTHDAY CAKE */
(function(){
  const canvas=document.getElementById('cakeCanvas'),ctx=canvas.getContext('2d');
  let blown=0;const TOTAL=5;
  function drawCake(){
    ctx.clearRect(0,0,300,320);
    ctx.beginPath();ctx.ellipse(150,295,130,18,0,0,Math.PI*2);ctx.fillStyle='rgba(201,168,76,0.12)';ctx.fill();ctx.strokeStyle='rgba(201,168,76,0.3)';ctx.lineWidth=1.5;ctx.stroke();
    const g1=ctx.createLinearGradient(45,195,255,275);g1.addColorStop(0,'#7a1530');g1.addColorStop(1,'#b5294e');
    ctx.beginPath();ctx.moveTo(50,268);ctx.lineTo(250,268);ctx.bezierCurveTo(250,290,50,290,50,268);ctx.lineTo(50,210);ctx.bezierCurveTo(50,192,250,192,250,210);ctx.lineTo(250,268);ctx.fillStyle=g1;ctx.fill();
    ctx.fillStyle='rgba(201,168,76,0.35)';ctx.fillRect(50,258,200,8);
    const g2=ctx.createLinearGradient(65,130,235,195);g2.addColorStop(0,'#6d1028');g2.addColorStop(1,'#a02040');
    ctx.beginPath();ctx.moveTo(65,192);ctx.lineTo(235,192);ctx.bezierCurveTo(235,210,65,210,65,192);ctx.lineTo(65,138);ctx.bezierCurveTo(65,120,235,120,235,138);ctx.lineTo(235,192);ctx.fillStyle=g2;ctx.fill();
    ctx.fillStyle='rgba(201,168,76,0.35)';ctx.fillRect(65,183,170,7);
    const g3=ctx.createLinearGradient(85,72,215,125);g3.addColorStop(0,'#5c0d1f');g3.addColorStop(1,'#8b1a38');
    ctx.beginPath();ctx.moveTo(85,128);ctx.lineTo(215,128);ctx.bezierCurveTo(215,145,85,145,85,128);ctx.lineTo(85,82);ctx.bezierCurveTo(85,65,215,65,215,82);ctx.lineTo(215,128);ctx.fillStyle=g3;ctx.fill();
    ctx.fillStyle='rgba(201,168,76,0.35)';ctx.fillRect(85,119,130,7);
    [[50,204],[85,204],[130,204],[175,204],[220,204]].forEach(([x,y])=>{ctx.beginPath();ctx.arc(x,y,7,0,Math.PI*2);ctx.fillStyle='rgba(201,168,76,0.25)';ctx.fill();});
    [[65,143],[100,143],[150,143],[200,143]].forEach(([x,y])=>{ctx.beginPath();ctx.arc(x,y,5,0,Math.PI*2);ctx.fillStyle='rgba(201,168,76,0.2)';ctx.fill();});
    ctx.font='italic 10px "Cormorant Garamond",serif';ctx.fillStyle='rgba(247,238,212,0.75)';ctx.textAlign='center';ctx.fillText('Happy Birthday',150,100);
    ctx.font='italic 9px "Cormorant Garamond",serif';ctx.fillStyle='rgba(201,168,76,0.8)';ctx.fillText('Begam Ji ♥',150,114);ctx.textAlign='left';
    const CX=[105,124,143,162,181];
    CX.forEach((x,i)=>{
      const isLit=i>=blown;
      const cg=ctx.createLinearGradient(x-5,42,x+5,65);const cols=['#c9a84c','#b5294e','#c9a84c','#b5294e','#c9a84c'];
      cg.addColorStop(0,cols[i]);cg.addColorStop(1,'#fff');ctx.fillStyle=cg;
      ctx.beginPath();if(ctx.roundRect)ctx.roundRect(x-5,42,10,24,3);else ctx.rect(x-5,42,10,24);ctx.fill();
      ctx.strokeStyle='rgba(0,0,0,0.2)';ctx.lineWidth=0.5;ctx.stroke();
      ctx.beginPath();ctx.moveTo(x,42);ctx.lineTo(x,36);ctx.strokeStyle='#666';ctx.lineWidth=1.5;ctx.stroke();
      if(isLit){
        const flick=Math.sin(Date.now()*0.01+i)*2;
        const fg=ctx.createRadialGradient(x+flick,28,1,x+flick,33,9);
        fg.addColorStop(0,'#fffbe8');fg.addColorStop(0.4,'#f5c518');fg.addColorStop(1,'rgba(245,70,0,0)');
        ctx.beginPath();ctx.moveTo(x+flick,22);ctx.bezierCurveTo(x+5+flick,28,x+4+flick,35,x+flick,37);ctx.bezierCurveTo(x-4+flick,35,x-5+flick,28,x+flick,22);ctx.fillStyle=fg;ctx.fill();
      }
    });
  }
  function animate(){drawCake();requestAnimationFrame(animate);}
  animate();
  canvas.addEventListener('click',()=>{if(blown<TOTAL){blown++;if(blown===TOTAL){document.getElementById('cakeInstruction').style.display='none';document.getElementById('cakeMsg').style.display='block';launchFireworks();}}});
})();

/* WISHING STARS */
const starsRow=document.getElementById('starsRow');
WISHES.forEach((msg,i)=>{
  const star=document.createElement('div');star.className='wish-star';star.textContent='✦';
  star.style.setProperty('--d',(1.2+i*0.4)+'s');star.style.color=i%2===0?'var(--gold)':'var(--rose3)';
  star.addEventListener('click',()=>{
    document.querySelectorAll('.wish-star').forEach(s=>s.classList.remove('granted'));
    star.classList.add('granted');
    const box=document.getElementById('wishGranted');box.style.display='block';
    document.getElementById('wishMsg').textContent=msg;launchFireworks();
  });
  starsRow.appendChild(star);
});

/* MODAL */
function openModal(html){document.getElementById('modalContent').innerHTML=html;document.getElementById('modal').classList.add('active');document.body.style.overflow='hidden';}
function closeModal(){document.getElementById('modal').classList.remove('active');document.body.style.overflow='';}
document.getElementById('modal').addEventListener('click',e=>{if(e.target===document.getElementById('modal'))closeModal();});

/* FIREWORKS */
function launchFireworks(){
  const c=document.getElementById('fwCanvas');c.width=window.innerWidth;c.height=window.innerHeight;c.style.display='block';
  const ctx=c.getContext('2d');const COLS=['#c9a84c','#e8d08a','#b5294e','#f0a0bb','#ffffff','#d4567a'];
  let particles=[];
  function burst(ox,oy){for(let i=0;i<90;i++){const angle=Math.random()*Math.PI*2,speed=2+Math.random()*7;particles.push({x:ox,y:oy,vx:Math.cos(angle)*speed,vy:Math.sin(angle)*speed-2,r:1.5+Math.random()*3,color:COLS[Math.floor(Math.random()*COLS.length)],a:1,decay:0.012+Math.random()*0.015});}}
  burst(c.width*0.35,c.height*0.35);setTimeout(()=>burst(c.width*0.65,c.height*0.4),250);setTimeout(()=>burst(c.width*0.5,c.height*0.25),500);
  let frame=0;
  function loop(){ctx.fillStyle='rgba(0,0,0,0.12)';ctx.fillRect(0,0,c.width,c.height);particles.forEach(p=>{p.x+=p.vx;p.y+=p.vy;p.vy+=0.07;p.a-=p.decay;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.color;ctx.globalAlpha=Math.max(0,p.a);ctx.fill();});ctx.globalAlpha=1;particles=particles.filter(p=>p.a>0);if(++frame<220)requestAnimationFrame(loop);else{ctx.clearRect(0,0,c.width,c.height);c.style.display='none';}}
  loop();
}

/* LOVE PULSE METER */
(function(){
  const LABELS=[[0,"Calculating love…"],[20,"Dil dhadakne laga ❤️"],[40,"Ishq barh raha hai 💕"],[60,"Mohabbat overload! 💖"],[80,"Dil full capacity pe hai 💘"],[99,"∞ — Koi limit nahi Begam Ji ke liye 💞"]];
  let v=0,dir=1,boostVal=0;
  const bar=document.getElementById('loveMeterBar'),label=document.getElementById('loveMeterLabel');
  if(!bar||!label)return;
  function tick(){boostVal=Math.max(0,boostVal-0.3);v+=dir*0.18+boostVal;if(v>=100){v=100;dir=-1;}if(v<=0){v=0;dir=1;}bar.style.width=v.toFixed(1)+'%';let lbl=LABELS[0][1];for(let i=0;i<LABELS.length;i++){if(v>=LABELS[i][0])lbl=LABELS[i][1];}label.textContent=lbl;requestAnimationFrame(tick);}
  tick();
  window.boostHeart=function(){boostVal=5;const h=document.getElementById('bigHeart');if(!h)return;h.style.transform='scale(2)';h.style.filter='drop-shadow(0 0 40px rgba(181,41,78,0.9))';setTimeout(()=>{h.style.transform='';h.style.filter='';},400);launchFireworks();};
})();

/* LOVE QUOTE TICKER */
(function(){
  const QUOTES=["Tum meri duniya ho ✦","Har saans mein teri yaad hai 🌹","Ishq tera, pyaar tera — sab tera ❤️","Aankhon mein bas tum ho 💫","Tum ho toh main hoon ✦","Meri jaan, meri Begam Ji 🥀","Har pal tujhe chahta hoon 💕","Dil ki dhadkan — Begam Ji ✦","Tu hai meri rooshni 🌙","Love you beyond words, always ❤️"];
  const track=document.getElementById('tickerTrack');if(!track)return;
  [...QUOTES,...QUOTES].forEach((q,i,a)=>{const span=document.createElement('span');span.className='ticker-item';span.innerHTML=q+(i<a.length-1?'<span class="ticker-sep">✦</span>':'');track.appendChild(span);});
})();

/* HEARTS RAIN */
(function(){
  const c=document.getElementById('heartsCanvas');if(!c)return;const ctx=c.getContext('2d');
  let W,H,hearts=[],heartsActive=false;
  function resize(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}
  window.addEventListener('resize',resize);resize();
  function spawnHeart(){const chars=['❤️','💕','💖','💗','💓','🌹','✦'];hearts.push({x:Math.random()*W,y:-30,vy:0.8+Math.random()*1.5,vx:(Math.random()-0.5)*0.5,size:16+Math.random()*20,a:0.7+Math.random()*0.3,ch:chars[Math.floor(Math.random()*chars.length)],rot:Math.random()*Math.PI*2,rotV:(Math.random()-0.5)*0.03});}
  function drawHearts(){ctx.clearRect(0,0,W,H);hearts.forEach(h=>{h.y+=h.vy;h.x+=h.vx;h.rot+=h.rotV;ctx.save();ctx.globalAlpha=h.a;ctx.font=h.size+'px serif';ctx.translate(h.x,h.y);ctx.rotate(h.rot);ctx.fillText(h.ch,0,0);ctx.restore();});hearts=hearts.filter(h=>h.y<H+40);if(heartsActive)requestAnimationFrame(drawHearts);else ctx.clearRect(0,0,W,H);}
  let spawnTimer=null;
  window.toggleHearts=function(){heartsActive=!heartsActive;const btn=document.getElementById('heartsToggle');if(heartsActive){c.style.opacity='1';spawnTimer=setInterval(spawnHeart,120);drawHearts();if(btn)btn.style.background='linear-gradient(135deg,#b5294e,#d4567a)';}else{c.style.opacity='0';clearInterval(spawnTimer);if(btn)btn.style.background='linear-gradient(135deg,#4a0f20,#7a1530)';}};
})();

/* HERO DATE */
const months=['January','February','March','April','May','June','July','August','September','October','November','December'];
const now=new Date();
document.getElementById('heroDate').textContent=months[now.getMonth()]+' '+now.getDate()+', '+now.getFullYear()+'  ·  From Mustafa, with endless love';

</script>
</body>
</html>
"""

def get_start_params():
    return {"year":RELATIONSHIP_START.year,"month":RELATIONSHIP_START.month-1,"day":RELATIONSHIP_START.day,"hour":RELATIONSHIP_START.hour,"minute":RELATIONSHIP_START.minute}

def build_final_html():
    import json
    s=get_start_params()
    h=COMPLETE_HTML
    h=h.replace("{{ start_year }}",str(s["year"]))
    h=h.replace("{{ start_month }}",str(s["month"]))
    h=h.replace("{{ start_day }}",str(s["day"]))
    h=h.replace("{{ start_hour }}",str(s["hour"]))
    h=h.replace("{{ start_minute }}",str(s["minute"]))
    h=h.replace("{{ photos_json }}",json.dumps(PHOTO_CONFIG))
    h=h.replace("{{ love_letter_json }}",json.dumps(LOVE_LETTER))
    return h

LOGIN_PAGE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Begam Ji — Darwaza</title>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300;1,400&family=Cinzel:wght@400;500&display=swap" rel="stylesheet">
  <style>
    *{margin:0;padding:0;box-sizing:border-box;}
    body{min-height:100vh;background:radial-gradient(ellipse 120% 100% at 50% 0%,#1a0530 0%,#06030a 60%);display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;overflow:hidden;position:relative;}
    canvas#stars{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;opacity:0.5;}
    .petals{position:fixed;inset:0;pointer-events:none;z-index:1;}.petal{position:absolute;font-size:1rem;animation:pfall linear forwards;opacity:0.5;}
    @keyframes pfall{0%{transform:translateY(-5vh) rotate(0deg);opacity:0;}8%{opacity:0.6;}100%{transform:translateY(105vh) rotate(360deg);opacity:0;}}
    .card{position:relative;z-index:5;background:rgba(10,5,18,0.78);backdrop-filter:blur(20px);border:1px solid rgba(201,168,76,0.22);border-radius:28px;padding:3.5rem 2.5rem 3rem;width:420px;max-width:92%;text-align:center;box-shadow:0 0 80px rgba(201,168,76,0.07),0 20px 60px rgba(0,0,0,0.7);animation:cardIn 1.2s cubic-bezier(.16,1,.3,1) both;}
    @keyframes cardIn{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
    .ornament{font-family:'Cinzel',serif;font-size:0.6rem;letter-spacing:0.5em;color:#c9a84c;text-transform:uppercase;opacity:0.7;margin-bottom:1.2rem;}
    h1{font-family:'Cinzel',serif;font-size:1.9rem;font-weight:400;color:#f5edd8;letter-spacing:0.06em;line-height:1.2;margin-bottom:0.6rem;}
    h1 span{display:block;background:linear-gradient(135deg,#c9a84c,#e8d08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
    .sub{font-style:italic;color:#a89580;font-size:1rem;margin-bottom:2.5rem;}
    .gold-bar{width:60px;height:1px;background:linear-gradient(90deg,transparent,#c9a84c,transparent);margin:0 auto 2rem;}
    input[type=password]{width:100%;padding:1rem 1.5rem;background:rgba(201,168,76,0.05);border:1px solid rgba(201,168,76,0.2);border-radius:50px;color:#f5edd8;font-family:'Cormorant Garamond',serif;font-size:1rem;text-align:center;outline:none;transition:border-color 0.3s,box-shadow 0.3s;margin-bottom:1.5rem;}
    input[type=password]:focus{border-color:rgba(201,168,76,0.6);box-shadow:0 0 20px rgba(201,168,76,0.1);}
    input[type=password]::placeholder{color:rgba(201,168,76,0.3);}
    button[type=submit]{width:100%;padding:1rem;background:linear-gradient(135deg,#7a1530,#b5294e);border:1px solid rgba(181,41,78,0.4);border-radius:50px;color:#f5edd8;font-family:'Cinzel',serif;font-size:0.75rem;letter-spacing:0.25em;text-transform:uppercase;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;}
    button[type=submit]:hover{transform:scale(1.02);box-shadow:0 10px 35px rgba(181,41,78,0.4);}
    .hint{margin-top:2rem;font-style:italic;color:rgba(168,149,128,0.5);font-size:0.82rem;}
  </style>
</head>
<body>
<canvas id="stars"></canvas>
<div class="petals" id="petalDiv"></div>
<div class="card">
  <p class="ornament">— A Private Invitation —</p>
  <h1>Welcome<span>Begam Ji</span></h1>
  <p class="sub">Only For My Favorite one..</p>
  <div class="gold-bar"></div>
  <form action="/check_password" method="post">
    <input type="password" name="password" placeholder="Enter the secret word…" autocomplete="off">
    <button type="submit">Enter ✦</button>
  </form>
  <p class="hint">Sirf Mustafa ke Begam Ji ke liye ❤️</p>
</div>
<script>
  const c=document.getElementById('stars'),ctx=c.getContext('2d');let W,H,stars=[];function resize(){W=c.width=innerWidth;H=c.height=innerHeight;}window.addEventListener('resize',resize);resize();for(let i=0;i<180;i++)stars.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1+0.2,a:Math.random(),s:(Math.random()-0.5)*0.004});function draw(){ctx.clearRect(0,0,W,H);stars.forEach(s=>{s.a+=s.s;if(s.a<0||s.a>1)s.s*=-1;ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fillStyle=`rgba(201,168,76,${s.a*0.7})`;ctx.fill();});requestAnimationFrame(draw);}draw();
  const PE=['🌹','✦','·','❧'];setInterval(()=>{const e=document.createElement('div');e.className='petal';e.textContent=PE[Math.floor(Math.random()*PE.length)];e.style.left=Math.random()*100+'vw';e.style.animationDuration=(5+Math.random()*8)+'s';e.style.fontSize=(0.6+Math.random()*0.7)+'rem';e.style.color=Math.random()>.5?'#c9a84c':'#b5294e';document.getElementById('petalDiv').appendChild(e);setTimeout(()=>e.remove(),13000);},700);
</script>
</body>
</html>"""

LOADING_PAGE = """<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="4;url=/surprise">
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preparing…</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500&family=Cormorant+Garamond:ital,wght@1,300&display=swap" rel="stylesheet">
  <style>*{margin:0;padding:0;box-sizing:border-box;}body{min-height:100vh;background:#06030a;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;}.box{text-align:center;padding:4rem 3rem;}.heart-ring{width:120px;height:120px;border-radius:50%;border:1px solid rgba(201,168,76,0.3);margin:0 auto 2.5rem;display:flex;align-items:center;justify-content:center;animation:ringPulse 1.8s ease-in-out infinite;}@keyframes ringPulse{0%,100%{box-shadow:0 0 0 0 rgba(201,168,76,0.3);}50%{box-shadow:0 0 0 20px rgba(201,168,76,0);}}.heart-icon{font-size:2.8rem;animation:heartbeat 1.2s ease-in-out infinite;}@keyframes heartbeat{0%,100%{transform:scale(1);}50%{transform:scale(1.18);}}h2{font-family:'Cinzel',serif;font-size:1.1rem;letter-spacing:0.2em;color:#c9a84c;text-transform:uppercase;margin-bottom:0.8rem;}p{font-style:italic;color:#a89580;font-size:1rem;}</style>
</head>
<body><div class="box"><div class="heart-ring"><div class="heart-icon">❤️</div></div><h2>Thoda Sa Intezaar</h2><p>Aapke liye kuch khaas tayyar ho raha hai…</p></div></body>
</html>"""

WRONG_PASSWORD_PAGE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hmm…</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400&family=Cormorant+Garamond:ital,wght@1,400&display=swap" rel="stylesheet">
  <style>*{margin:0;padding:0;box-sizing:border-box;}body{min-height:100vh;background:#06030a;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;}.box{background:rgba(10,5,18,0.85);border:1px solid rgba(181,41,78,0.25);border-radius:24px;padding:3.5rem 2.5rem;max-width:400px;width:90%;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.6);}.icon{font-size:3rem;margin-bottom:1.5rem;display:block;}h2{font-family:'Cinzel',serif;font-size:1rem;letter-spacing:0.25em;color:#b5294e;text-transform:uppercase;margin-bottom:1rem;}p{font-style:italic;color:#a89580;font-size:1rem;line-height:1.7;margin-bottom:1.5rem;}a{display:inline-block;padding:0.75rem 2.5rem;border:1px solid rgba(201,168,76,0.3);border-radius:50px;color:#c9a84c;font-family:'Cinzel',serif;font-size:0.65rem;letter-spacing:0.25em;text-transform:uppercase;text-decoration:none;transition:background 0.25s;}a:hover{background:rgba(201,168,76,0.08);}</style>
</head>
<body><div class="box"><span class="icon">🔒</span><h2>Galat Code</h2><p>Apne sohar Mustafa se password le aaiye — woh zaroor batayenge 🥺</p><a href="/">Wapas Jaiye →</a></div></body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def login():
    return HTMLResponse(content=LOGIN_PAGE)

@app.post("/check_password", response_class=HTMLResponse)
async def check_password(password: str = Form(...)):
    if password.strip().upper() == CORRECT_PASSWORD:
        return HTMLResponse(content=LOADING_PAGE)
    return HTMLResponse(content=WRONG_PASSWORD_PAGE)

@app.get("/surprise", response_class=HTMLResponse)
async def surprise():
    return HTMLResponse(content=build_final_html())

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
