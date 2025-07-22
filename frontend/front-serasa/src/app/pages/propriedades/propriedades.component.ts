import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';

interface Produtor {
  id: number;
  nome: string;
  documento: string;
  cidade: string;
  estado: string;
}

interface Propriedade {
  id: number;
  nome: string;
  cidade: string;
  estado: string;
  area_total: number;
  area_agricultavel: number;
  area_vegetacao: number;
  produtor_id: number;
}

@Component({
  selector: 'app-propriedades',
  templateUrl: './propriedades.component.html',
  styleUrls: ['./propriedades.component.scss']
})
export class PropriedadesComponent implements OnInit {
  produtores: Produtor[] = [];
  propriedades: Propriedade[] = [];
  propriedadeForm: FormGroup;
  displayedColumns: string[] = [
    'nome',
    'cidade',
    'estado',
    'area_total',
    'area_agricultavel',
    'area_vegetacao',
    'produtor',
    'actions'
  ];

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private snackBar: MatSnackBar
  ) {
    this.propriedadeForm = this.fb.group({
      nome: ['', Validators.required],
      cidade: ['', Validators.required],
      estado: ['', Validators.required],
      area_total: ['', [Validators.required, Validators.min(0)]],
      area_agricultavel: ['', [Validators.required, Validators.min(0)]],
      area_vegetacao: ['', [Validators.required, Validators.min(0)]],
      produtor_id: ['', Validators.required]
    });
  }

  ngOnInit() {
    this.loadProdutores();
    this.loadPropriedades();
  }

  loadProdutores() {
    this.http.get<Produtor[]>('http://localhost:8000/produtores/').subscribe({
      next: data => this.produtores = data,
      error: () => this.snackBar.open('Erro ao carregar produtores', 'Fechar', { duration: 3000 })
    });
  }

  loadPropriedades() {
    this.http.get<Propriedade[]>('http://localhost:8000/propriedades/').subscribe({
      next: data => this.propriedades = data,
      error: () => this.snackBar.open('Erro ao carregar propriedades', 'Fechar', { duration: 3000 })
    });
  }

  createPropriedade() {
    if (this.propriedadeForm.invalid) return;

    this.http.post<Propriedade>('http://localhost:8000/propriedades/', this.propriedadeForm.value).subscribe({
      next: (propriedade) => {
        // Ao invés de push direto, crie uma nova referência para o array
        this.propriedades = [...this.propriedades, propriedade];

        this.propriedadeForm.reset();
        this.snackBar.open('Propriedade criada com sucesso', 'Fechar', { duration: 3000 });
      },
      error: () => this.snackBar.open('Erro ao criar propriedade', 'Fechar', { duration: 3000 })
    });
  }

  deletePropriedade(id: number) {
    this.http.delete(`http://localhost:8000/propriedades/${id}`).subscribe({
      next: () => {
        this.propriedades = this.propriedades.filter(p => p.id !== id);
        this.snackBar.open('Propriedade excluída', 'Fechar', { duration: 3000 });
      },
      error: () => this.snackBar.open('Erro ao excluir propriedade', 'Fechar', { duration: 3000 })
    });
  }

  getProdutorNome(produtor_id: number): string {
    const produtor = this.produtores.find(p => p.id === produtor_id);
    return produtor ? produtor.nome : '';
  }
}
