import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CulturaSafraComponent } from './cultura-safra.component';

describe('CulturaSafraComponent', () => {
  let component: CulturaSafraComponent;
  let fixture: ComponentFixture<CulturaSafraComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CulturaSafraComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CulturaSafraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
