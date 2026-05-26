#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import re
ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / 'blog' / 'posts'
POSTS.mkdir(parents=True, exist_ok=True)
topics = [
('client offboarding checklist for freelancers','Client Offboarding Checklist for Freelancers'),
('how to ask for a client testimonial','How to Ask for a Client Testimonial'),
('freelance project handoff email','Freelance Project Handoff Email'),
('referral request script for consultants','Referral Request Script for Consultants'),
('case study template for freelancers','Case Study Template for Freelancers'),
('repeat work email after project','Repeat Work Email After a Project'),
('final project delivery email template','Final Project Delivery Email Template')]
def slugify(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
existing={p.name for p in POSTS.glob('*.html')}
for keyword,title in topics:
    name=slugify(title)+'.html'
    if name not in existing:
        today=datetime.now(timezone.utc).date().isoformat()
        html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>{title}</title><meta name="description" content="A practical guide to {keyword} for freelancers and solo service providers."/><link rel="canonical" href="https://bkhjr1297.github.io/client-offboarding-kit/blog/posts/{name}"/><meta name="robots" content="index, follow"/></head><body><main><p><a href="../../">Back to Client Offboarding Kit</a></p><article><p>Published {today} · Keyword focus: {keyword}</p><h1>{title}</h1><p>If you sell services, the end of a project is the best time to clarify the result, collect proof, and make the next step easy.</p><ol><li>Summarize the completed work.</li><li>Link final files and usage notes.</li><li>Ask for a short testimonial.</li><li>Ask for one referral.</li><li>Document the result for a case study.</li><li>Offer the next logical service.</li><li>Schedule a follow-up reminder.</li></ol><p><a href="../../#builder">Build your free offboarding email</a></p><p>Business workflow support only. Not legal, tax, accounting, privacy, or compliance advice.</p></article></main></body></html>'''
        (POSTS/name).write_text(html)
        break
posts=sorted(POSTS.glob('*.html'))
items=[]; urls=['https://bkhjr1297.github.io/client-offboarding-kit/','https://bkhjr1297.github.io/client-offboarding-kit/blog/']
for p in posts:
    text=p.read_text(errors='ignore'); m=re.search(r'<title>(.*?)</title>', text); title=m.group(1) if m else p.stem
    items.append(f'<li><a href="posts/{p.name}">{title}</a></li>'); urls.append(f'https://bkhjr1297.github.io/client-offboarding-kit/blog/posts/{p.name}')
(ROOT/'blog/index.html').write_text('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>Client Offboarding Blog</title><meta name="description" content="Client offboarding guides for freelancers."/><link rel="canonical" href="https://bkhjr1297.github.io/client-offboarding-kit/blog/"/><meta name="robots" content="index, follow"/></head><body><main><p><a href="../">Back to free builder</a></p><h1>Client offboarding guides</h1><ul>'+'\n'.join(items)+'</ul></main></body></html>')
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join(f'  <url><loc>{u}</loc></url>' for u in urls)+'\n</urlset>\n')
print('daily blog generation complete')
