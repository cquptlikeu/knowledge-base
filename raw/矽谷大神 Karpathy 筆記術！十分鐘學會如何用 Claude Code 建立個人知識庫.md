---
title: "矽谷大神 Karpathy 筆記術！十分鐘學會如何用 Claude Code 建立個人知識庫"
source: "https://www.youtube.com/watch?v=FdSO1Yhr76I&t=178s"
author:
  - "[[Paula 寶拉]]"
published: 2026-04-14
created: 2026-07-06
description: "兩篇文章丟進去，AI 自己幫你整理成個人知識庫這集實作 Andrej Karpathy 分享的個人知識庫方法：不用 RAG、不用向量資料庫，只靠 Obsidian + Claude Code 就能做出一個會自己找連結、自己補缺口的知識庫。跟著做幾分鐘就能開始用，適合想把筆記用起來的人。(00:00) Karpathy 分享的方法在社群上瘋傳(00:36) 原始貼文重點：Wiki 會自"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=FdSO1Yhr76I)

兩篇文章丟進去，AI 自己幫你整理成個人知識庫  
  
這集實作 Andrej Karpathy 分享的個人知識庫方法：不用 RAG、不用向量資料庫，只靠 Obsidian + Claude Code 就能做出一個會自己找連結、自己補缺口的知識庫。  
  
跟著做幾分鐘就能開始用，適合想把筆記用起來的人。  
  
(00:00) Karpathy 分享的方法在社群上瘋傳  
(00:36) 原始貼文重點：Wiki 會自己成長、會自己健檢  
(01:39) 系統架構：Raw、Wiki、Index、Log、claude.md  
(02:58) 需要的工具：Obsidian + Claude Code  
(03:33) 建立 Obsidian Vault 並初始化資料夾結構  
(05:27) 用 Obsidian Clipper 收集文章  
(06:44) 讓 Claude 讀文章、自動建立 Wiki  
(07:17) Graph View 看跨文章的自動連結  
(07:52) Wiki 頁面結構：Concepts、Entity、Source  
(08:29) 實際用法：問問題、找知識缺口、AI 補資料  
(09:53) 這方法跟傳統 RAG 的差異  
(10:43) 四個限制與適用場景  
(11:22) 總結  
  
Obsidian 下載  
https://obsidian.md  
  
Obsidian Web Clipper  
https://chromewebstore.google.com/detail/obsidian-web-clipper  
  
llm-wiki  
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Transcript

### Karpathy 分享的方法在社群上瘋傳

**0:00** · Drop in two articles, and AI generates this itself — no sorting, no tagging, no database. A Silicon Valley legend shared this method and it went viral.

**0:08** · Today I'll actually build it for you.

**0:10** · Have you ever read an article and thought, this is important, I have to remember it — and two weeks later you can't even recall where you saw it?

**0:17** · Or you diligently saved bookmarks, screenshots, dumped it all into a notes app, open it a month later — bookmarks everywhere, but you have no idea where to even start.

**0:25** · And here's an even more common problem: article A mentions a concept, article B hits the same idea from a completely different angle, but because they live in different places, you never notice the connection.

### 原始貼文重點：Wiki 會自己成長、會自己健檢

**0:36** · Recently Andrej Karpathy — former head of AI at Tesla, and one of the co-founders of OpenAI — shared a method on X to solve this exact problem.

**0:45** · His approach is to hand articles to AI, and after reading, AI auto-organizes them into a Wiki — with summaries, an index, and links between related concepts, all stored on your own computer as a pile of markdown files.

**0:56** · He made a few key points in that thread I really liked.

**0:59** · First — you ask AI a question, it answers, and you save the answer back into the Wiki.

**1:02** · That means your knowledge base gets richer the more you use it.

**1:05** · Every lookup accumulates into the system.

**1:09** · Second — you can let AI do periodic health checks on your Wiki.

**1:13** · It looks for contradictions or gaps in your notes, and will even tell you, "Your coverage in this area is thin, want to add a few more articles?"

**1:21** · Then he said something I really liked: you'll almost never need to edit the Wiki yourself, because it's the LLM's turf — building and maintaining it is all AI's job.

**1:31** · He organized about 100 articles this way. He said he originally thought he'd need RAG, but letting the LLM maintain the index itself was enough.

### 系統架構：Raw、Wiki、Index、Log、claude.md

**1:39** · Before we build, let's go through the system's structure, so the demo makes more sense later.

**1:45** · The whole knowledge base is just an Obsidian Vault.

**1:48** · Inside, there are two main folders.

**1:50** · The first is Raw — where you drop things in.

**1:53** · Articles, PDFs, any raw material you want to organize — it all lands here first.

**1:57** · Think of it as an inbox.

**2:00** · The second is Wiki — where AI puts the organized version.

**2:04** · It splits the Raw material into Wiki pages. Each page has a summary, tags, and links to other related pages.

**2:11** · Inside the Wiki folder there's an Index — this part is key.

**2:14** · It's the directory of the whole knowledge base, listing every page and category.

**2:19** · When AI looks something up, it doesn't have to read every file.

**2:22** · It just reads the Index first to know where to go.

**2:26** · That's why this method stays fast even with hundreds of pages.

**2:31** · There's also a Log — everything AI does: which article it read, which pages it added, which Wiki links it changed — all logged here.

**2:39** · So you can trace back what happened, and AI also knows what it did before and won't redo it.

**2:44** · Finally there's a claude.md file — it's the instruction manual for AI.

**2:49** · It tells AI what this project is, how to organize data, and how to write the Wiki.

**2:53** · Every time you open Claude Code, it reads this file first, so it always knows what to do.

### 需要的工具：Obsidian + Claude Code

**2:58** · So how do we start?

**2:59** · You only need two tools. First, Obsidian — a free notes app.

**3:03** · It lets you see connections between notes as a graph.

**3:07** · Just download it at obsidian.md — completely free.

**3:10** · Second is Claude Code — the AI engine that reads, organizes, and links.

**3:15** · That's it. Installation steps are in my previous video, linked in the description.

**3:20** · Takes a few minutes to set up.

**3:22** · Now I'll walk you through building it.

**3:24** · If you don't want to miss tutorials like this, hit subscribe if you haven't. I'm Paula, this channel is all about testing and teaching AI tools.

### 建立 Obsidian Vault 並初始化資料夾結構

**3:33** · Okay, after installing Obsidian, open it up and click Create.

**3:38** · Name it whatever. Since this is Andrej Karpathy's demo, I'll call mine AKDEMO.

**3:44** · Pick a location you can find later, then click Create.

**3:53** · I'm using Antigravity to drive Claude.

**3:56** · If you don't know how to use it, I have a tutorial — link in the description.

**4:01** · Here I'm opening the AKDEMO folder I just made.

**4:06** · Open the terminal and type "claude".

**4:12** · Now we paste Karpathy's concept in. Let's go back to X.

**4:18** · He put his prompt in this Gist — so we click it.

**4:23** · After clicking, you end up on this screen.

**4:26** · This is the content of his prompt.

**4:29** · Below, lots of people are discussing how they do it themselves.

**4:32** · Worth a scroll if you're curious.

**4:35** · Back at the top, click Raw, and select-all, copy.

**4:40** · Back in Antigravity, paste it in.

**4:43** · Then ask Claude: based on this concept, build out the whole knowledge base structure for me.

**4:50** · And we wait a bit.

**4:52** · Okay, it's done.

**4:54** · You can see it created the Raw folder for us.

**4:57** · Inside there's an Assets folder, and there's also the Wiki folder.

**5:01** · And there's the Index page, and the Log — which records this initialization run.

**5:07** · We can also open claude.md to take a look.

**5:10** · You can see it wrote out a lot about this project — how to organize data, the formatting rules for the Wiki.

**5:16** · That's the instruction manual for AI we mentioned.

**5:18** · Every time you open Claude Code, it reads this file first, so we don't have to re-explain what the project is.

**5:26** · The structure is ready.

### 用 Obsidian Clipper 收集文章

**5:27** · How do we get articles into our Wiki?

**5:30** · The easiest way is a Chrome extension called Obsidian Clipper.

**5:37** · Add it to Chrome.

**5:44** · Once installed, pin it.

**5:47** · Let's grab two articles.

**5:50** · The first is from the author of The Almanack of Naval Ravikant, about reading being the foundation of learning — start with what you enjoy.

**5:57** · Click the Obsidian extension, and here, change the folder to Raw — matching our folder name.

**6:05** · Then click Add to Obsidian.

**6:12** · You can see it saved into the Raw folder.

**6:18** · Let's add a second article.

**6:20** · Also from Naval — about finding your own specific knowledge, the kind of work that feels like play to you but looks like work to others.

**6:28** · Same thing — click the Obsidian extension, change it to Raw, Add to Obsidian.

**6:37** · And it gets ingested the same way.

**6:41** · Back to Antigravity to drive Claude Code.

### 讓 Claude 讀文章、自動建立 Wiki

**6:46** · Both articles are now in.

**6:49** · Open the terminal, and tell Claude: there are new articles in Raw, please ingest them.

**6:57** · As it reads them, it breaks out the concepts and people, builds a wiki page for each, with a summary and tags, and links to other related pages. It also updates the index, adding new pages into the directory.

**7:13** · So let's wait a moment.

### Graph View 看跨文章的自動連結

**7:17** · Claude Code is done. Let's hop back to Obsidian.

**7:22** · You can see it built out this graph.

**7:25** · Let's check the graph view. Two articles — each has its own cluster of nodes.

**7:31** · But some of them cross over.

**7:33** · Like the "continuous learning" node — it caught the overlap between the two and formed a shared node.

**7:40** · This is what makes the system powerful — AI finds the common ground between articles on its own and wires them up automatically.

**7:48** · The more articles you add, the more cross-article links you get, and the more useful it becomes.

### Wiki 頁面結構：Concepts、Entity、Source

**7:52** · Done with the graph — let's look at what's inside the Wiki.

**7:56** · Concepts — it takes ideas from those two articles and gives each its own page, explaining the definition and key points.

**8:06** · Entity — the people mentioned in those two articles, with notes on who they are and which concepts they connect to.

**8:16** · Source — each original article we fed in, recording what it covered and which concepts and key points it maps to.

**8:24** · These three page types link to each other — that's what the graph shows.

### 實際用法：問問題、找知識缺口、AI 補資料

**8:29** · Okay, so what can this system do?

**8:32** · First — ask it questions. Like, how does Naval's idea of specific knowledge relate to reading?

**8:38** · One is about making money, the other is about reading — so how do these two actually connect?

**8:44** · We type that in and wait for the answer.

**8:47** · A cross-article question like this — you might not spot the connection on your own, but AI can. So it answers based on what we fed into the system.

**8:59** · We can also ask something more concrete: if I don't know what my specific knowledge is, what would Naval suggest I do?

**9:10** · It synthesizes both articles to answer.

**9:14** · Naval's view — first cultivate curiosity, find what you enjoy, notice what feels like play to you but looks like work to others.

**9:24** · Second use case — finding knowledge gaps.

**9:27** · You can ask it: based on the current Wiki, which areas are under-covered?

**9:34** · It'll help you fill those gaps.

**9:36** · It points out exactly where you can add more.

**9:41** · It can also run searches for us.

**9:43** · So the third, more advanced use — it can pull in extra material to fill those gaps.

**9:49** · That's the practical side of this Wiki.

### 這方法跟傳統 RAG 的差異

**9:53** · If you follow AI, you've probably heard of RAG.

**9:56** · That's when AI searches a database to answer a question.

**10:00** · The biggest difference with Karpathy's method — no vector database, no embeddings at all.

**10:07** · Traditional RAG chunks articles, turns them into vectors, stores them in a database.

**10:12** · Queries rely on similarity search, and the setup bar is higher.

**10:16** · This method is just a pile of markdown files plus an index.

**10:20** · AI finds things by reading the directory and links — no similarity search.

**10:25** · Upside: simple to set up, easy to maintain, cost is basically just AI tokens.

**10:30** · Downside: it has a scale limit.

**10:32** · Around 100 articles works well in practice.

**10:35** · But for tens of thousands of documents you'd probably need a real RAG system.

**10:39** · For most individual users though, this method is plenty.

### 四個限制與適用場景

**10:43** · As usual, let's talk about the limits.

**10:46** · First — Claude Code costs money, you need a paid plan. Obsidian is free.

**10:51** · Second — ingest takes time, a few minutes per article.

**10:55** · Throw 30 articles in at once and you'll wait 10 to 15 minutes.

**11:00** · Third — it's built for personal scale.

**11:02** · Dozens to a few hundred articles: fine.

**11:04** · For tens of thousands of documents, you'll likely want other tools.

**11:09** · Fourth — bigger knowledge base, more tokens.

**11:12** · Every query, AI reads the index and the relevant wiki pages. More content means more tokens in the context.

**11:18** · If you're paying per API call, that cost adds up.

### 總結

**11:22** · Andrej Karpathy's method — two folders plus an AI and you're done.

**11:26** · If this makes you want to try it, just start.

**11:29** · Drop in two or three articles and see how it feels.

**11:32** · That's it for this episode. Leave a comment and tell me what topic you want next.

**11:36** · Like, subscribe, ring the bell — see you next time.