# Shared Configuration

The `config/` directory centralizes linting rules, formatter presets, schema definitions, and other reusable configuration artifacts that apply across the monorepo.

## Suggested Layout

```
config/
  ├── lint/          ESLint, Flake8, or other linting presets.
  ├── format/        Prettier, Black, or Stylua configurations.
  └── schemas/       Shared JSON/YAML schemas used by multiple services.
```

As tooling is adopted, create subdirectories (e.g., `config/lint/eslint.json`) and have services reference these files rather than duplicating configuration. This keeps the developer experience consistent and reduces drift.

For now, this directory serves as a placeholder until concrete tooling is introduced.
