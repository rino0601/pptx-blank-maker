# coding=utf-8
import click
from pptx import Presentation

__author__ = 'rino0601'


@click.command()
@click.argument('source_pptx_file', type=click.File('r'))
def cli(source_pptx_file):
    click.echo(u"Welcome, Before we start converting, There is some things you have to know.")
    click.echo(u"   1. This tool does not support videos which you upload tistory directly.\n"
               u"   They seems only play able on tistory blog.\n"
               u"   If you have good idea for this, please contribute this project.\n"
               u"   2. This tool ignore comments, track backs, tags and categories. \n"
               u"   There is some different with jekyll and tistory's system.\n"
               u"   I didn't have enough time for consider that.\n"
               u"   3. If you want bring your picture and attachment from tistory, that blog has to be alive.\n"
               u"   (backup_with_attachment.xml isn't available for now.)\n")
    click.confirm(u'Do you want to continue?', abort=True)
    # with click.progressbar(posts, label=u"Converting posts...") as bar:
    prs = Presentation(source_pptx_file)

    # text_runs will be populated with a list of strings,
    # one for each text run in presentation
    text_runs = []

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text_runs.append(run.text)
                    print(run.text)
