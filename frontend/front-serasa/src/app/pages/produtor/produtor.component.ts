import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatTableDataSource } from '@angular/material/table';

interface Produtor {
  id: number;
  nome: string;
  documento: string;
  cidade: string;
  estado: string;
}

@Component({
  selector: 'app-produtor',
  templateUrl: './produtor.component.html',
  styleUrls: ['./produtor.component.scss']
})
export class ProdutorComponent implements OnInit {
  produtorForm: FormGroup;
  produtores = new MatTableDataSource<Produtor>([]);
  displayedColumns: string[] = ['nome', 'documento', 'cidade', 'estado', 'actions'];

  private baseUrl = 'http://localhost:8000/produtores/';

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private snackBar: MatSnackBar
  ) {
    this.produtorForm = this.fb.group({
      nome: ['', Validators.required],
      documento: ['', Validators.required],
      cidade: ['', Validators.required],
      estado: ['', Validators.required],
    });
  }

  ngOnInit() {
    this.loadProdutores();
  }

  loadProdutores() {
    this.http.get<Produtor[]>(this.baseUrl).subscribe({
      next: data => this.produtores.data = data,
      error: () => this.snackBar.open('Erro ao carregar produtores', 'Fechar', { duration: 3000 })
    });
  }

  createProdutor() {
    if (this.produtorForm.invalid) return;

    this.http.post<Produtor>(this.baseUrl, this.produtorForm.value).subscribe({
      next: produtor => {
        // Atualiza datasource adicionando novo produtor
        this.produtores.data = [...this.produtores.data, produtor];
        this.produtorForm.reset();
        this.snackBar.open('Produtor criado com sucesso', 'Fechar', { duration: 3000 });
      },
      error: () => this.snackBar.open('Erro ao criar produtor', 'Fechar', { duration: 3000 })
    });
  }

  deleteProdutor(id: number) {
    this.http.delete(`${this.baseUrl}${id}`).subscribe({
      next: () => {
        // Atualiza datasource removendo produtor excluído
        this.produtores.data = this.produtores.data.filter(p => p.id !== id);
        this.snackBar.open('Produtor excluído', 'Fechar', { duration: 3000 });
      },
      error: () => this.snackBar.open('Erro ao excluir produtor', 'Fechar', { duration: 3000 })
    });
  }
}
