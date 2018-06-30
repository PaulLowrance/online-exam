import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Exam } from '../exams/exam.model';
import { API_URL } from '../env';


@Injectable(/* {
  providedIn: 'root'
} */)
export class ExamsApiService {

  constructor(private http: HttpClient) {

  }

  getExams(): Observable<Exam[]> {
   return this.http.get<any>(`${API_URL}/exams`);
  }
}
