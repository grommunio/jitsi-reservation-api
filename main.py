# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

from api import app
from endpoints import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
