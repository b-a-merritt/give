import sys

from give.app import Give
from give.commands.add import add
from give.commands.branch import branch
from give.commands.checkout import checkout
from give.commands.commit import commit
from give.commands.files import files_cmd
from give.commands.init import init
from give.commands.status import status
from give.commands.unadd import unadd
from give.commands.uncommit import uncommit


app = Give()

app.register('add', add)
app.register('branch', branch)
app.register('checkout', checkout)
app.register('commit', commit)
app.register('files', files_cmd)
app.register('init', init)
app.register('status', status)
app.register('unadd', unadd)
app.register('uncommit', uncommit)

app.run(*sys.argv[1:])