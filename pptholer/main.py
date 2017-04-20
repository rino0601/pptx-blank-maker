# coding=utf-8
import click

__author__ = 'rino0601'


@click.command()
@click.argument('tistory_backup_min', type=click.File('r'))
def cli(tistory_backup_min):
    """
    This command make _post & _drafts directory from your tistory_backup.xml file.
    """
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
