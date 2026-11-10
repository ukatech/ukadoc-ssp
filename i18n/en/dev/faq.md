# Development FAQ

Frequently asked questions for developers.<br>
These answers may help when you're not sure how to handle bug reports you've received.<br>
However, they don't cover information specific to each ghost's SHIORI, so see the explanations for each SHIORI in the [Development links](links.md).

- [Questions about development basics](#開発の基本についての質問)
- [Questions about bugs](#バグについての質問)

## Questions about development basics

### Q: I want to make a ghost! Where should I start?

**A1:** Once you have a general idea of what kind of ghost you want to make, you will probably start by preparing two things.

One is a shell, or a set of character images. You can either draw them yourself or ask someone else to draw them (as you might expect).<br>
If you want to prepare them yourself, see the section on creating shells in “ukadoc,” listed in the [Development links](links.md#仕様書リファレンス).<br>
Otherwise, fortunately, there are shells called “free shells” that are available for anyone to use.<br>
The “freeshell wiki” in the [Development links](links.md#素材プログラムツール配布元) should help you find free shells.

The other thing you need besides a shell is the core of the ghost, called SHIORI.<br>
The way you build the ghost's brain—how it talks and acts in different situations—varies greatly depending on the SHIORI you use.<br>
The [Development links](links.md#shiori) describe some of the most common SHIORI implementations.<br>
Use that as a reference and choose one that suits you and your ghost.

Once you have both a shell and SHIORI, you're ready to start creating your ghost. From this point on, the work depends almost entirely on the SHIORI you chose.<br>
So it may be a good idea to start by reading a site that explains your SHIORI in detail.<br>
We've listed as many of those sites as possible in the [Development links](links.md#shiori).

### Q: How do I publish my ghost?

**A1:** If you don't need to add a network update feature to your ghost, it's easy.<br>
All you need to do is package all your ghost's files into a nar (or zip) archive and publish it.<br>
You may be able to use an online storage service (Dropbox, Google Drive, OneDrive, etc.) or a suitable file uploader.<br>
You will need to prepare a few settings and files for this. For details, read the “Creating files for distribution” page in “ukadoc,” listed in the [Development links](links.md#仕様書リファレンス).

However, if you plan to add a network update feature, you'll also need to prepare a server.<br>
A server doesn't have to be anything special. You can use a service normally used to host a personal website, such as a rental server, rental space, or website publishing service.<br>
However, depending on the server settings and terms of use, it may not be suitable for publishing a ghost.<br>
You can look into what kinds of servers other ghost authors use, or read the “If you want to distribute a ghost” article in the [Development links](links.md#その他).

Once you have a server, all you need to do is upload your ghost's files to it.<br>
As with a regular website, you can upload files using FTP.<br>
For details, read the “Supporting network updates” page in “ukadoc,” listed in the [Development links](links.md#仕様書リファレンス).<br>
※If you aren't sure how to upload files to a server using FTP, try searching for “publish a website.”

In addition to general FTP software, you can also install the “Ghost Distribution Automation System” distributed by “Seibihan,” listed in the [Development links](links.md). This can help you avoid some of the work and problems involved in uploading your ghost.<br>
The initial installation and setup take a little effort, but please give it a try.

### Q: Can I distribute SSP bundled with a ghost?

**A1:** This isn't prohibited, but we don't recommend it because it can cause many technical problems.

### Q: How can I promote the content I've created?

**A1:** You can register it with “disc-2” or “Ghost Capture Sakura,” listed in the [Links](../about/links.md). If you have time, please also try “GHOST TOWN.”<br>
There are also threads in “Kairanban” where you can promote your work. Twitter may be the quickest place to get a response.

### Q: Where can I find the official SSP reference?

**A1:** It's “UKADOC,” at the top of the [Development links](links.md).

### Q: I've looked into various things about creating content, but still can't find the answer. Is there somewhere I can ask for help?

**A1:** The development forum at “Ukateki Forum,” listed in the [Links](../about/links.md#コミュニティなど), is a place for that.<br>
Even if it looks like nobody is around, if you ask a question, someone will probably show up from somewhere.<br>
As of 2015, Twitter is where the most people are. If you have an account, try posting your question with the “#伺か” or “#ukagaka” tag. Someone will almost certainly see it (and sometimes you'll get surrounded by enthusiastic helpers, so please don't be scared off).

## Questions about bugs

### Q: I see a lot of entries in the error log. Is it okay to ignore them?

**A1:** It depends. For details, see the [Script log](scriptlog.md#エラーログ) page.

### Q: I get an MD5 mismatch error, and network updates aren't working.

**A1:** Did you modify any files targeted for updating after creating the update files (update.txt/update2.dau)?<br>
Also, when uploading the update files over FTP, did you transfer them in ASCII mode?<br>
To help prevent these kinds of mistakes, you can use the “Ghost Distribution Automation System,” distributed by “Seibihan” and listed in the [Links](../about/links.md).

**A2:** Depending on the server settings, uploaded files may have been modified.<br>
For example, some free website hosting services occasionally try to forcibly insert advertisements even into text files.
