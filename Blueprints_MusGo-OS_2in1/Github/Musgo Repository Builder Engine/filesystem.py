#!/usr/bin/env python3
"""
MusGo-OS Knowledge Engine
Filesystem Utility

Author : Dhani Yuliawan
License: Proprietary

Production Ready
"""

from __future__ import annotations

import hashlib
import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Optional


SUPPORTED_EXTENSIONS = {
    ".md",
    ".markdown",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
}


@dataclass(slots=True)
class FileInfo:
    absolute_path: Path
    relative_path: Path
    repository: str
    filename: str
    extension: str
    size: int
    sha256: str


class FileSystem:

    def __init__(self, root: Path):

        self.root = Path(root).resolve()

        if not self.root.exists():
            raise FileNotFoundError(self.root)

    ##########################################################
    # DIRECTORY
    ##########################################################

    def ensure_directory(self, path: Path):

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def remove_directory(self, path: Path):

        if path.exists():

            shutil.rmtree(path)

    ##########################################################
    # FILE
    ##########################################################

    def remove_file(self, path: Path):

        if path.exists():

            path.unlink()

    def touch(self, path: Path):

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.touch(exist_ok=True)

    ##########################################################
    # HASH
    ##########################################################

    @staticmethod
    def sha256(file: Path):

        h = hashlib.sha256()

        with file.open("rb") as f:

            while True:

                chunk = f.read(1024 * 1024)

                if not chunk:
                    break

                h.update(chunk)

        return h.hexdigest()

    ##########################################################
    # WALKER
    ##########################################################

    def walk(self):

        yield from os.walk(self.root)

    def iter_files(
        self,
        extensions: Optional[Iterable[str]] = None,
    ) -> Iterator[Path]:

        normalized = None

        if extensions:

            normalized = {
                ext.lower()
                if ext.startswith(".")
                else "." + ext.lower()
                for ext in extensions
            }

        for current_root, _, files in self.walk():

            current_root = Path(current_root)

            for name in files:

                file = current_root / name

                if normalized:

                    if file.suffix.lower() not in normalized:
                        continue

                yield file

    ##########################################################
    # KNOWLEDGE
    ##########################################################

    def iter_skill_files(self):

        for file in self.iter_files(["md"]):

            if file.name.upper() == "SKILL.MD":

                yield file

    def iter_markdown(self):

        yield from self.iter_files(
            SUPPORTED_EXTENSIONS,
        )
    
  ##########################################################
# PATH
##########################################################

def relative(self, file: Path) -> Path:

    return file.resolve().relative_to(self.root)


def repository_name(self, file: Path) -> str:

    relative = self.relative(file)

    if not relative.parts:
        return "UNKNOWN"

    return relative.parts[0]


##########################################################
# VALIDATION
##########################################################

@staticmethod
def is_hidden(file: Path) -> bool:

    return any(
        part.startswith(".")
        for part in file.parts
    )


@staticmethod
def is_binary(file: Path) -> bool:

    try:

        with file.open("rb") as fp:

            chunk = fp.read(4096)

        return b"\x00" in chunk

    except Exception:

        return True


@staticmethod
def is_supported(file: Path) -> bool:

    return file.suffix.lower() in SUPPORTED_EXTENSIONS


##########################################################
# METADATA
##########################################################

def build_info(
    self,
    file: Path,
) -> FileInfo:

    stat = file.stat()

    return FileInfo(
        absolute_path=file.resolve(),
        relative_path=self.relative(file),
        repository=self.repository_name(file),
        filename=file.name,
        extension=file.suffix.lower(),
        size=stat.st_size,
        sha256=self.sha256(file),
    )


def collect(
    self,
    extensions: Optional[Iterable[str]] = None,
) -> list[FileInfo]:

    results = []

    for file in self.iter_files(extensions):

        if self.is_hidden(file):
            continue

        if self.is_binary(file):
            continue

        results.append(
            self.build_info(file)
        )

    return results


##########################################################
# DIRECTORY SIZE
##########################################################

@staticmethod
def directory_size(path: Path) -> int:

    total = 0

    for root, _, files in os.walk(path):

        root = Path(root)

        for name in files:

            file = root / name

            try:

                total += file.stat().st_size

            except OSError:

                continue

    return total


##########################################################
# EMPTY DIRECTORY CLEANER
##########################################################

@staticmethod
def remove_empty(path: Path):

    for root, dirs, _ in os.walk(
        path,
        topdown=False,
    ):

        for directory in dirs:

            current = Path(root) / directory

            try:

                current.rmdir()

            except OSError:

                pass