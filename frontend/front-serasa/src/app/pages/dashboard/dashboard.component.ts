import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ChartType } from 'chart.js';  // IMPORTAÇÃO DO TIPO

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  dashboard: any;

  pieChartLabelsEstado: string[] = [];
  pieChartDataEstado: number[] = [];

  pieChartLabelsCultura: string[] = [];
  pieChartDataCultura: number[] = [];

  pieChartLabelsUsoSolo: string[] = ['Agricultável', 'Vegetação'];
  pieChartDataUsoSolo: number[] = [];

  pieChartOptions = {
    responsive: true,
  };

  // Aqui tipamos corretamente para o ChartType
  pieChartType: ChartType = 'pie';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('http://localhost:8000/dashboard/').subscribe({
      next: (data: any) => {
        this.dashboard = data;

        this.pieChartLabelsEstado = data.propriedades_por_estado.map((x: any) => x.estado);
        this.pieChartDataEstado = data.propriedades_por_estado.map((x: any) => x.quantidade);

        this.pieChartLabelsCultura = data.culturas.map((x: any) => x.nome);
        this.pieChartDataCultura = data.culturas.map((x: any) => x.quantidade);

        this.pieChartDataUsoSolo = [
          data.uso_solo.agricultavel,
          data.uso_solo.vegetacao
        ];
      },
      error: (err) => {
        console.error('Erro ao carregar dados do dashboard', err);
      }
    });
  }
}
