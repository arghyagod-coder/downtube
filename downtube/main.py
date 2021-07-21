import click
import os
import pytube
from youtube_search import *
import subprocess as sb
from tqdm import tqdm
from youtube_search import *
import time
from click_help_colors import HelpColorsGroup, HelpColorsCommand

@click.version_option('0.1.6', prog_name='downtube')
@click.group(
    cls=HelpColorsGroup, help_headers_color="blue", help_options_color="green"
)
def main():
    '''
Download Youtube Videos fast and easily with DownTube
    '''
    pass

@main.command('init', help='Initialize downtube to get started')
def init():
    try:
        os.mkdir((os.path.join(os.path.expanduser("~"), ".downtube")))
        os.mknod((os.path.join(os.path.expanduser("~"), ".downtube", "config.txt")))
    except FileExistsError as e:
        print('File already exists')

@main.command('config', help="Setup your default video resolution")
@click.option('--resolution', '-dr')
def config(resolution):
    click.secho('\nYou can choose one of the following resolutions as default\n\n', fg='cyan')
    click.secho('Video:\n\n', fg='yellow')
    click.secho('1) 144p\n2) 240\n3) 360p\n4) 480p\n5) 720p\n8) 1080p\n\n', fg='red')
    if resolution!=None:
        with open(os.path.join(os.path.expanduser("~"), ".downtube", "config.txt"), 'w') as f:
            f.write(resolution)
        click.secho(f'Set resolution to {resolution} successfully!',fg='green')

@main.command('dlvl', help="Download Video by URL")
@click.argument('url')
@click.option('--dir', '-d', is_flag=True)
@click.option('--resolution', '-r')
def download_by_link(url, resolution, dir):
    try:
        if dir:
            os.chdir(os.path.join((os.path.expanduser("~")), 'Downloads'))
        URL = pytube.YouTube(url)
        avail = []
        flist = ['1080p', '720p', '480p', '360p', '240p', '144p']
        for stream in URL.streams:
            for i in flist:
                if i in str(stream):
                    avail.append(i)
                else:
                    pass
        if resolution in (i for i in avail):
            try:
                for i in tqdm (range (100), desc="Loading…"):
                    URL.streams.filter(res=resolution, audio_codec='mp4a.40.2').first().download()

                click.secho('The video was downloaded successfully', fg='green')
            except Exception as e:
                click.secho('Error!! 3 possible reasons:\n\n- The file trying to be reached did not support audio, hence DownTube avoided it, try using another resolution (recommended: 720p or 360p)\n-Invalid Youtube Link\n- Invalid Resolution', fg='red')
        elif resolution==None:
            try:
                with open(os.path.join(os.path.expanduser("~"), ".downtube", "config.txt"), 'r') as f:
                    dres = f.read() 
                for i in tqdm (range (100), desc="Loading…"):
                    URL.streams.filter(res=dres, audio_codec='mp4a.40.2').first().download()

            except Exception as e:
                click.secho('Error!! 3 possible reasons:\n\n- The file trying to be reached did not support audio, hence DownTube avoided it, try using another resolution (recommended: 720p or 360p)\n- Invalid Youtube Link\n- Invalid Resolution', fg='red')
    except Exception:
        click.secho('An unexpected error occured', fg="red")
    
@main.command('dlyt', help="Download Video by Search")
@click.argument('search')
@click.option('--dir', '-d', is_flag=True)
@click.option('--resolution', '-r')
def download_from_yt(search, resolution, dir):
    try:
        if dir:
            os.chdir(os.path.join((os.path.expanduser("~")), 'Downloads'))
        results = YoutubeSearch(str(search), max_results=1).to_dict()
        sp = results[0]["id"]
        URL = pytube.YouTube('https://youtube.com/' + sp)
        avail = []
        flist = ['1080p', '720p', '480p', '360p', '240p', '144p']
        for stream in URL.streams:
            for i in flist:
                if i in str(stream):
                    avail.append(i)
                else:
                    pass
        if resolution in (i for i in avail):
            try:
                click.secho(results[0]["title"], fg='yellow')
                click.secho(results[0]["channel"]+'\n', fg='yellow')
                for i in tqdm (range (100), desc="Downloading…"):
                    URL.streams.filter(res=resolution, audio_codec='mp4a.40.2').first().download()

                click.secho('The video was downloaded successfully', fg='green')
            except Exception as e:
                click.secho('Error!! 3 possible reasons:\n\n- The file trying to be reached did not support audio, hence DownTube avoided it, try using another resolution (recommended: 720p or 360p)\n-Invalid Youtube Link\n- Invalid Resolution', fg='red')
        elif resolution==None:
            try:
                with open(os.path.join(os.path.expanduser("~"), ".downtube", "config.txt"), 'r') as f:
                    dres = f.read() 
                click.secho(results[0]["title"], fg='yellow')
                click.secho(results[0]["channel"]+'\n', fg='yellow')
                for i in tqdm (range (100), desc="Loading…"):
                    URL.streams.filter(res=dres, audio_codec='mp4a.40.2').first().download()

            except Exception as e:
                click.secho('Error!! 3 possible reasons:\n\n- The file trying to be reached did not support audio, hence DownTube avoided it, try using another resolution (recommended: 720p or 360p)\n- Invalid Youtube Link\n- Invalid Resolution', fg='red')
    except Exception as e:
        click.secho('An unexpected error occured', fg="red")
    
@main.command('dayt', help="Download Audio by Search")
@click.argument('search')
@click.option('--dir', '-d', is_flag=True)
def download_from_yt(search, dir):
    try:
        if dir:
            os.chdir(os.path.join((os.path.expanduser("~")), 'Downloads'))

        results = YoutubeSearch(str(search), max_results=1).to_dict()
        sp = results[0]["id"]
        URL = pytube.YouTube('https://youtube.com/' + sp)
        click.secho(results[0]["title"], fg='yellow')
        click.secho(results[0]["channel"]+'\n', fg='yellow')
        video = URL.streams.filter(only_audio=True, audio_codec='mp4a.40.2').first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        for i in tqdm (range (100), desc="Downloading…"):
            time.sleep(0.01)
        click.secho('The video was downloaded successfully', fg='green')
    except Exception as e:
        click.secho('Error!! 2 possible reasons:\n\n-Invalid Youtube Link\n- Invalid Resolution', fg='red')

@main.command('dlal', help="Download Audio by URL")
@click.argument('url')
@click.option('--dir', '-d', is_flag=True)
def download_from_yt(url, dir):
    try:
        if dir:
            os.chdir(os.path.join((os.path.expanduser("~")), 'Downloads'))

        URL = pytube.YouTube(url)
        results = YoutubeSearch(str(URL.title), max_results=1).to_dict()
        click.secho(URL.title, fg='yellow')
        click.secho(results[0]["channel"]+'\n', fg='yellow')
        video = URL.streams.filter(only_audio=True, audio_codec='mp4a.40.2').first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        for i in tqdm (range (100), desc="Downloading…"):
            time.sleep(0.01)
        click.secho('The video was downloaded successfully', fg='green')
    except Exception as e:
        print(e)
        click.secho('Error!! 2 possible reasons:\n\n-Invalid Youtube Link\n- Invalid Resolution', fg='red')


if __name__=="__main__":
    main()