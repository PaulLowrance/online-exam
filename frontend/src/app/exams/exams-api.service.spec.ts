import { TestBed, inject } from '@angular/core/testing';

import { ExamsApiService } from './exams-api.service';
describe('Exams2Service', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ExamsApiService]
    });
  });

  it('should be created', inject([ExamsApiService], (service: ExamsApiService) => {
    expect(service).toBeTruthy();
  }));
});
