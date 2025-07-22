import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';

interface CulturaSafra {
  id: number;
  nome: string;
  ano: number;
  variedade: string;
  area_plantada: number;
  propriedade_id: number;
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
  selector: 'app-cultura-safra',
  templateUrl: './cultura-safra.component.html',
  styleUrls: ['./cultura-safra.component.scss']
})
export class CulturaSafraComponent implements OnInit {
  culturasSafra: CulturaSafra[] = [];
  propriedades: Propriedade[] = [];
  culturaForm: FormGroup;
  displayedColumns: string[] = ['nome', 'ano', 'variedade', 'area_plantada', 'propriedade_nome', 'actions'];

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private snackBar: MatSnackBar
  ) {
    this.culturaForm = this.fb.group({
      nome: ['', Validators.required],
      ano: ['', [Validators.required, Validators.min(1900), Validators.max(new Date().getFullYear())]],
      variedade: ['', Validators.required],
      area_plantada: ['', [Validators.required, Validators.min(0)]],
      propriedade_id: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    this.loadPropriedades();
    this.loadCulturasSafra();
  }

  loadPropriedades() {
    this.http.get<Propriedade[]>('http://localhost:8000/propriedades/?skip=0&limit=100').subscribe({
      next: data => this.propriedades = data,
      error: () => this.snackBar.open('Erro ao carregar propriedades', 'Fechar', { duration: 3000 })
    });
  }

  loadCulturasSafra() {
    this.http.get<CulturaSafra[]>('http://localhost:8000/culturasafra/').subscribe({
      next: data => this.culturasSafra = data,
      error: () => this.snackBar.open('Erro ao carregar culturas safra', 'Fechar', { duration: 3000 })
    });
  }

  createCulturaSafra() {
    if (this.culturaForm.invalid) return;

    this.http.post<CulturaSafra>('http://localhost:8000/culturasafra/', this.culturaForm.value).subscribe({
      next: (cultura) => {
        this.culturasSafra = [...this.culturasSafra, cultura];
        this.culturaForm.reset();
        this.snackBar.open('Cultura Safra criada com sucesso', 'Fechar', { duration: 3000 });
      },
      error: () => this.snackBar.open('Erro ao criar cultura safra', 'Fechar', { duration: 3000 })
    });
  }

  deleteCulturaSafra(id: number) {
    this.http.delete(`http://localhost:8000/culturasafra/${id}`).subscribe({
      next: () => {
        this.culturasSafra = this.culturasSafra.filter(c => c.id !== id);
        this.snackBar.open('Cultura Safra excluída', 'Fechar', { duration: 3000 });
      },
      error: () => this.snackBar.open('Erro ao excluir cultura safra', 'Fechar', { duration: 3000 })
    });
  }

  getPropriedadeNome(propriedade_id: number): string {
    return this.propriedades.find(p => p.id === propriedade_id)?.nome || '';
  }
}
