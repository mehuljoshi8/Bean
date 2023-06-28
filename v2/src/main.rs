use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    // 2326 is bean spelled out :)
    let listener = TcpListener::bind("127.0.0.1:2326").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();
    
    let status_line = "HTTP /1.1 200 OK";
    let contents = fs::read_to_string("templates/hello.html").unwrap();
    let len = contents.len();

    let response = format!("{status_line}\r\nContent-length: {len}\r\n\r\n{contents}");

    stream.write_all(response.as_bytes()).unwrap();
}
