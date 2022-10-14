import pathlib

import pytest

from py_mono_tools.test_utils import vagrant_ssh
import typing as t


@pytest.mark.parametrize("vagrant", ["docker_module"], indirect=["vagrant"])
@pytest.mark.parametrize("conf_name", ["", "-n example_docker_module"])
class TestCli:
    def test_help(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(command=f"poetry run pmt {conf_name} --help", cwd=cwd.absolute())
        assert b"Usage: pmt" in result

    def test_isort(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint --check -s isort",
            cwd=cwd.absolute(),
        )
        assert b"main.py Imports are incorrectly sorted and/or formatted" in result

    def test_black(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint --check -s black",
            cwd=cwd.absolute(),
        )
        assert b"Lint result: black 0 " in result

    def test_py_doc_string_formatter(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint --check -s py_doc_string_formatter",
            cwd=cwd.absolute(),
        )
        assert b"Lint result: py_doc_string_formatter 0" in result

    def test_bandit(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint -s bandit",
            cwd=cwd.absolute(),
        )
        assert b"Lint result: bandit 0" in result

    def test_flake8(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint -s flake8",
            cwd=cwd.absolute(),
        )
        assert b"F401" in result

    def test_mypy(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint -s mypy",
            cwd=cwd.absolute(),
        )
        assert b"Missing return statement" in result

    def test_pydocstyle(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint -s pydocstyle",
            cwd=cwd.absolute(),
        )
        assert b"__init__.py:1 at module level:" in result

    @pytest.mark.skip()
    def test_pylint(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint -s pylint",
            cwd=cwd.absolute(),
        )
        assert b"Lint result: pylint 0" in result

    @pytest.mark.skip()
    def test_pip_audit(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint -s pip-audit",
            cwd=cwd.absolute(),
        )
        assert b"Lint result: pip-audit 0" in result

    @pytest.mark.skip()
    def test_all(self, vagrant: pathlib.Path, conf_name: t.Optional[str]) -> None:
        cwd = vagrant
        returncode, result = vagrant_ssh(
            command=f"poetry run pmt {conf_name} lint --check",
            cwd=cwd.absolute(),
        )
        assert b"Lint result: pip-audit 0" in result
