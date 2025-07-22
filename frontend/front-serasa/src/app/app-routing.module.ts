import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { ProdutorComponent } from './pages/produtor/produtor.component';
import { PropriedadesComponent } from './pages/propriedades/propriedades.component';
import { CulturaSafraComponent } from './pages/cultura-safra/cultura-safra.component';

export const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'produtor', component: ProdutorComponent },
  { path: 'propriedades', component: PropriedadesComponent },
  { path: 'cultura-safra', component: CulturaSafraComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
