import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { Book } from './book';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root',
})
export class HeroService {

  constructor(private messageService: MessageService) { }

  getHeroes(): Observable<Book[]> {
    const heroes = of(BOOKS);
    this.messageService.add('HeroService: fetched heroes');
    return heroes;
  }
}