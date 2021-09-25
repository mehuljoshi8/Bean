package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

//Sessions are the objects that record shots made/missed in Bean
type Session struct {
	StartTime string
	EndTime   string
}

type Shots struct {
	Made      int
	Attempted int
}

var idToSession map[int]Session
var midrangeLeftCorner map[int]Shots

//todo: add a function here that parses the made/attempted string
func parseString(str string) {

}

//todo: add a

func main() {
	//currently trying to get a minimal working product
	//then i'll work on the server...
	spots := [11]string{"midrange_left_corner",
		"midrange_left_wing",
		"midrange_top_key",
		"midrange_right_wing",
		"midrange_right_corner",
		"three_left_corner",
		"three_left_wing",
		"three_top_key",
		"three_right_wing",
		"three_right_corner",
		"free_throw"}

	idToSession = make(map[int]Session)
	midrangeLeftCorner = make(map[int]Shots)

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Basketball Enters the Application Network (BEAN)")
	fmt.Println("To not add data for a particular location just press ENTER")

	for {
		for _, s := range spots {
			fmt.Print(s + ": ")
			txt, _ := reader.ReadString('\n')
			txt = strings.Replace(txt, "\n", "", -1)
			parseString(txt)
		}
	}
}
