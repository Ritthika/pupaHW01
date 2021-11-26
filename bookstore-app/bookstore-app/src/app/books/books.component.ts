import { Component, OnInit } from '@angular/core';
import { Book } from '../book';


@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {
  book1: Book = {
    id: 1,
    bookname: 'Windstorm',
    amount: 1,
    picurl: 'http//:.....',
    price: 100,

  };

  constructor() { }

  ngOnInit(): void {
  }

}
