package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

//Sessions are the objects that record shots made/missed in Bean
type Session struct {
	StartTime string
	EndTime   string
}

type FG struct {
	Made      int
	Attempted int
}

var idToSession map[int]Session
var midrangeLeftCorner map[int]FG

/**
 * The parseString function takes in a string str that
 * is formatted via the made/attempted format and returns
 * an FG struct storing the made/attempted data.
 */
func parseString(str string) FG {
	res := strings.Split(str, "/")
	m, _ := strconv.Atoi(res[0])
	a, _ := strconv.Atoi(res[1])
	return FG{m, a}
}

//todo: add a function that

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
	midrangeLeftCorner = make(map[int]FG)

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Basketball Enters the Application Network (BEAN)")
	fmt.Println("To not add data for a particular location just press ENTER")

	for {
		for _, s := range spots {
			fmt.Print(s + ": ")
			txt, _ := reader.ReadString('\n')
			txt = strings.Replace(txt, "\n", "", -1)
			matches, _ := regexp.MatchString("^[0-9]*/[0-9]*$", txt)
			if matches {
				parseString(txt)
			} else {
				fmt.Println("Please try to enter your string in the form of made/attempted")
				os.Exit(0)
			}
		}
	}
}
