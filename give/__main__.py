import sys

from give.app import Give
from give.commands.add import add
from give.commands.branch import branch
from give.commands.checkout import checkout
from give.commands.commit import commit
from give.commands.files import files
from give.commands.init import init
from give.commands.status import status
from give.commands.unadd import unadd
from give.commands.uncommit import uncommit

from give.constants import GIVE_CMD_ADD
from give.constants import GIVE_CMD_BRANCH
from give.constants import GIVE_CMD_CHECKOUT
from give.constants import GIVE_CMD_COMMIT
from give.constants import GIVE_CMD_FILES
from give.constants import GIVE_CMD_INIT
from give.constants import GIVE_CMD_STATUS
from give.constants import GIVE_CMD_UNADD
from give.constants import GIVE_CMD_UNCOMMIT


app = Give()

app.register(GIVE_CMD_ADD, add)
app.register(GIVE_CMD_BRANCH, branch)
app.register(GIVE_CMD_CHECKOUT, checkout)
app.register(GIVE_CMD_COMMIT, commit)
app.register(GIVE_CMD_FILES, files)
app.register(GIVE_CMD_INIT, init)
app.register(GIVE_CMD_STATUS, status)
app.register(GIVE_CMD_UNADD, unadd)
app.register(GIVE_CMD_UNCOMMIT, uncommit)

app.run(*sys.argv[1:])