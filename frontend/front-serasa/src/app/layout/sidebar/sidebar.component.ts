import { Component } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  template: `
    <mat-nav-list>
      <a mat-list-item routerLink="/dashboard" routerLinkActive="active-link">Dashboard</a>
    </mat-nav-list>
  `,
  styles: [`
    .active-link {
      font-weight: bold;
      color: #388e3c;
    }
  `]
})
export class SidebarComponent {}
