use std::net::TcpListener;

fn main() {
    // 2326 is bean spelled out :)
    let listener = TcpListener::bind("127.0.0.1:2326").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        println!("connection established!");
    }
}
