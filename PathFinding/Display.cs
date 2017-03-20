using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PathFinding
{
    class Position {
        private int x;
        private int y;

        //Initializers
        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        //Public Funtions
        public int getX() {
            return this.x;
        }

        public int getY() {
            return this.x;
        }
    }

    class Display
    {
        private Position origin;
        private Position end;
        private int size;

        //Private Functions
        //Create a Random origin position
        private Position createRandomPosition() {
            Random rnd = new Random();
            int x = rnd.Next(0, size);
            int y = rnd.Next(0, size);
            Position pos = new Position(x, y);

            return pos;
        }

        //Initializers
        public Display(char size) {
            this.size = size;
        }

        //Public Functions
        public void createOrigin() {
            this.origin = createRandomPosition();
        }

        public void createEnd() {
            this.end = createRandomPosition();
        }
    }
}
