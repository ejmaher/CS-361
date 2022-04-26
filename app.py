# Author: Evan Maher
# Date: 4/25/2022
# Description: Minimum Viable Product - CS 361

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
