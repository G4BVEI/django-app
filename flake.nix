{
  description = "Django dev environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      pythonEnv = pkgs.python313.withPackages (
        ps: with ps; [
          django
          djangorestframework
          psycopg2
          python-dotenv
        ]
      );
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pythonEnv
          pkgs.libpqxx # Common C++ library for Postgres
          pkgs.postgresql # Provides 'pg_config' which psycopg2 often looks for
        ];

        shellHook = ''
          echo "Welcome to your Django dev environment!"
          python --version
          django-admin --version
        '';
      };
    };
}
