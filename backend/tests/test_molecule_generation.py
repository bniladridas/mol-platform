from rdkit import Chem

from src.main import MoleculeGenerator


def test_generate_random_molecule():
    base_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin
    generator = MoleculeGenerator()

    # Generate a molecule
    generated_mol = generator.generate_random_molecule(base_smiles)

    # Check that a valid molecule was generated
    assert generated_mol is not None
    assert isinstance(generated_mol, Chem.Mol)

    # Check that the generated molecule is different from the base molecule
    generated_smiles = Chem.MolToSmiles(generated_mol)
    assert generated_smiles != base_smiles


def test_molecule_properties():
    base_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin
    generator = MoleculeGenerator()

    # Generate a molecule
    generated_mol = generator.generate_random_molecule(base_smiles)
    generated_smiles = Chem.MolToSmiles(generated_mol)

    # Calculate properties
    properties = generator.calculate_properties(generated_smiles)

    # Check that properties are calculated
    assert "Molecular Weight" in properties
    assert "LogP" in properties
    assert "H-Bond Donors" in properties
    assert "H-Bond Acceptors" in properties
    assert "Topological Polar Surface Area" in properties

    # Check that properties are numeric
    for prop_value in properties.values():
        assert isinstance(prop_value, (int, float))


def test_mutation_strategies():
    base_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"  # Aspirin

    # Test multiple mutation strategies
    mutation_methods = [
        MoleculeGenerator._add_random_substituent,
        MoleculeGenerator._modify_bond_order,
        MoleculeGenerator._swap_atom,
    ]

    for method in mutation_methods:
        mol = Chem.MolFromSmiles(base_smiles)
        mutated_mol = method(mol)

        assert mutated_mol is not None
        assert isinstance(mutated_mol, Chem.Mol)
        assert Chem.MolToSmiles(mutated_mol) != base_smiles


def test_generate_with_custom_mutations():
    base_smiles = "CCO"  # Ethanol
    generator = MoleculeGenerator()

    # Test with specific mutation types
    generated_mol = generator.generate_random_molecule(
        base_smiles, mutation_types=["substituent"]
    )
    assert generated_mol is not None

    generated_mol = generator.generate_random_molecule(
        base_smiles, mutation_types=["atom_swap"]
    )
    assert generated_mol is not None

    # Test with empty mutation types (should use defaults)
    generated_mol = generator.generate_random_molecule(base_smiles, mutation_types=[])
    assert generated_mol is not None
