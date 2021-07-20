# DownTube
## `Downtube` : A simple CLI for downloading youtube videos in video/audio format

NOTE: I dont support downloading stuff illegally, be sure to use it for legal purposes and creative commons licensed videos only

## Install

```
pip3 install downtube 
```

## Dependencies
+ `click` 
+ `click_help_colors`
+ `pytube`
+ `tqdm`
+ `youtube_search`

## Built with
+ `Python 3.9.6` 

## Supported Platforms:

+ Operating System = Cross-Platform

## How to use

Open powershell for Windows or Terminal for Linux/Mac and  and type ```dtube```

If the following result comes, then you have successfully installed downtube on your system

```bash

  Download Youtube Videos fast and easily with DownTube

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  config  Setup your default video resolution
  dayt    Download Audio by Search
  dlal    Download Audio by URL
  dlvl    Download Video by URL
  dlyt    Download Video by Search
  init    Initialize downtube to get started
```

else, try the above steps again!

#### Setup

First you need to setup downtube for yourself

Procedure:

- Run `dtube config -dr <resolution>`to set your preferred default video resolution for download. You can check options for resolutions by executing `dtube config`

- Now you are set up to use downtube

**Most of the time only 360p and 720p videos support audio, so they are recommended over any other resolution**

##### Download video from search terms :

```
dtube dlyt {Search Terms} -r {resolution(optional)}
```

For example:

```
dtube dlyt Despacito_Song -r 360p
```
The first result from your search terms will be downloaded to your current folder

Giving a resolution is completely optional. If you dont provide it, the video will be downloaded in your default resolution.

**Most of the time only 360p and 720p videos support audio, so they are recommended over any other resolution**

##### Download video from URL

```
dtube dlvl {Video URL} -r {resolution(optional)}
```

For example:

```
dtube dlvl 'https://www.youtube.com/watch?v=kJQP7kiw5Fk' -r 360p
```
The video redirected by your url will be downloaded to your current folder

Giving a resolution is completely optional. If you dont provide it, the video will be downloaded in your default resolution.

**Most of the time only 360p and 720p videos support audio, so they are recommended over any other resolution**

##### Download audio from Search Terms

```
dtube dayt {Search Terms}
```

For example:

```
dtube dayt Despacito_Song
```
The first result from your search terms will be downloaded to your current folder in AUDIO format

##### Download audio from URL

```
dtube dlat {Video URL}
```

For example:

```
dtube dlal 'https://www.youtube.com/watch?v=kJQP7kiw5Fk
```
The video redirected by your url will be downloaded to your current folder in AUDIO format

#### Developers
- [Arghya Sarkar](https://github.com/arghyagod-coder)


### Developer Tools

- [Visual Studio Code](https://github.com/microsoft/vscode)

- [Python 3.9.6](https://python.org)

- [Git](https://git-scm.com)

- [Python Poetry](https://python-poetry.org/)

## License

License © 2021-Present Arghya Sarkar

This repository is licensed under the MIT license. See [LICENSE](https://github.com/arghyagod-coder/downtube/blob/main/LICENSE) for details.

## Special Notes

- Contribution is appreciated! 
- If you see anything uncomfortable or not working, file an issue in [the issue page](https://github.com/arghyagod-coder/downtube/issues). Issues aren't ignored by the developers
- Thanks for seeing my project!