---
name: merge-conflict-resolver
description: Guides AI agents through systematic git merge conflict resolution — analyzing conflict markers, identifying root causes, selecting optimal resolution strategies, and verifying fixes. Covers content conflicts, rename/delete conflicts, binary file conflicts, and submodule conflicts across all languages.
_agensi: "8b8c9b15-ee1f-4405-b114-d8ca13ef3bfc"
---

# Merge Conflict Resolver

Guides AI agents through systematic git merge conflict resolution with analysis, strategy selection, and verification.

## When to Use

- After `git merge`, `git rebase`, or `git pull` produces conflicts
- Before resolving conflicts in a shared branch to avoid accidental data loss
- When conflict markers span multiple files and the resolution is unclear
- As part of a PR integration workflow to ensure clean merges

## Conflict Anatomy

Every conflict block follows this structure:

```
<<<<<<< HEAD
our changes (current branch)
=======
their changes (incoming branch)
>>>>>>> branch-name
```

For 3-way merges (during `git rebase`):

```
<<<<<<< HEAD
our changes (current branch state)
||||||| merged common ancestor
original content (before either change)
=======
their changes (incoming changes)
>>>>>>> branch-name
```

## Resolution Workflow

### Step 1: Assess Scope

1. Run `git diff --name-only --diff-filter=U` to list all conflicted files
2. Count total conflicts: `git diff --check | grep -c 'conflict'`
3. Classify each conflict by type:
   - **Content conflict**: Same lines modified differently in both branches
   - **Add/add conflict**: File added independently in both branches
   - **Rename/rename**: File renamed differently in both branches
   - **Rename/delete**: One branch renamed, other deleted
   - **Modify/delete**: One branch modified, other deleted
   - **Binary conflict**: Binary file changed in both branches
   - **Submodule conflict**: Submodule commit diverged

### Step 2: Understand the Cause

For each conflict, determine why it occurred:

| Cause Pattern | Indicator | Resolution Complexity |
|---------------|-----------|----------------------|
| Divergent edits to same function | Both sides modify overlapping lines | Medium |
| One side reformatted, other side changed logic | Diff is mostly whitespace vs. substantive | Low |
| Independent feature additions in same file | Changes are in different regions but overlap at boundaries | Low |
| Conflicting dependency versions | `package.json`, `requirements.txt`, `go.mod` changed in both | Medium |
| API contract change vs. consumer change | One branch changes interface, other changes caller | High |

### Step 3: Select Resolution Strategy

Choose one strategy per conflict:

| Strategy | When to Use | Command |
|----------|-------------|---------|
| **Accept Ours** | Current branch has the correct version; incoming changes are superseded | `git checkout --ours <file>` then `git add <file>` |
| **Accept Theirs** | Incoming branch has the correct version; our changes are superseded | `git checkout --theirs <file>` then `git add <file>` |
| **Manual Merge** | Both sides have valuable changes that need to be combined | Edit file, remove conflict markers, combine changes |
| **Rebase Instead** | Linear history preferred; conflicts are easier to resolve one commit at a time | `git rebase <target>` instead of `git merge` |
| **Squash & Re-apply** | Too many conflicts; squash feature branch and re-apply on top of target | `git reset --soft`, then re-commit on updated target |

### Step 4: Resolve Content Conflicts

For each content conflict block:

1. **Read both sides** — understand what each branch is trying to do
2. **Identify the intent** — is this a bug fix, feature addition, refactor, or format change?
3. **Choose the resolution**:
   - If both changes are needed: merge them, preserving logic from both
   - If one supersedes the other: pick the correct side
   - If they are incompatible: flag for human review with explanation
4. **Remove all conflict markers** — `<<<<<<<`, `=======`, `>>>>>>>`, and `|||||||` (for rebase)
5. **Preserve surrounding context** — do not accidentally delete adjacent code

#### Language-Specific Resolution Notes

**Python:**
- Watch for indentation mismatches after merging — mixed tabs/spaces cause SyntaxError
- Check that import statements are consistent (no duplicates, no missing imports)
- Verify decorator order is preserved if both sides modified decorators

**JavaScript/TypeScript:**
- Check that import/export statements are not duplicated
- Verify that function signatures match their call sites after merging
- Look for missing semicolons or unmatched braces after manual merge

**Go:**
- Ensure import blocks are consolidated (Go enforces sorted imports)
- Check that struct field additions from both sides are preserved
- Run `go fmt` after resolution to normalize formatting

**Java:**
- Verify that import statements are not duplicated
- Check that method signatures and annotations from both sides are preserved
- Ensure closing braces are balanced

**SQL/Migrations:**
- **Critical**: Never drop a column or table that the other branch depends on
- Check that migration file numbering does not conflict
- Verify foreign key constraints are consistent

### Step 5: Resolve Add/Add Conflicts

When the same file was created independently in both branches:

1. Read both versions to understand the different implementations
2. If they serve the same purpose: merge the best parts into one file
3. If they serve different purposes: rename one and update all references
4. If one is clearly superior: accept that version and delete the other

### Step 6: Resolve Rename/Delete and Modify/Delete Conflicts

| Scenario | Resolution |
|----------|-----------|
| Branch A renamed `foo.py` → `bar.py`, Branch B deleted `foo.py` | Keep the rename (`bar.py`), confirm deletion intent |
| Branch A modified `config.yaml`, Branch B deleted it | Discuss with team — is the file still needed? If yes, restore modified version |
| Branch A renamed `foo.py` → `bar.py`, Branch B renamed `foo.py` → `baz.py` | Pick one name or create both with different purposes |

Commands:
```bash
# Keep the renamed file
git add bar.py
git rm foo.py  # if it still exists as a conflict artifact

# Or restore deleted file with modifications
git checkout --theirs config.yaml
git add config.yaml
```

### Step 7: Resolve Binary File Conflicts

Binary files (images, compiled assets, databases) cannot be merged line-by-line:

1. Run `git ls-files --unmerged` to see the conflicting versions
2. Compare both versions: `git show :2:<file> > /tmp/ours.bin && git show :3:<file> > /tmp/theirs.bin`
3. Decide which version to keep, or create a new merged version manually
4. Use `git add <file>` to mark as resolved

### Step 8: Verify Resolution

After resolving all conflicts:

1. **Check no markers remain**: `grep -rn '<<<<<< \|======\|>>>>>> ' --include='*' .`
2. **Verify build passes**: Run the project's build/compile step
3. **Run tests**: Execute the test suite to catch integration issues
4. **Check file count**: `git status` should show all conflicts resolved
5. **Review the merge commit**: `git diff --staged` to see what will be committed

#### Verification Checklist

- [ ] Zero conflict markers remaining in any file
- [ ] Project compiles/builds without errors
- [ ] Test suite passes (or known failures are documented)
- [ ] No accidental deletions of unrelated code
- [ ] Import statements are consistent and not duplicated
- [ ] Indentation/formatting is uniform
- [ ] File encoding is preserved (no BOM insertion, no encoding changes)

### Step 9: Complete the Merge

```bash
# After all conflicts are resolved and verified
git add <all-resolved-files>
git commit -m "Merge <branch>: resolve N conflicts in <areas>"

# For rebase
git rebase --continue
```

## Common Conflict Patterns

### Pattern 1: Whitespace/Formatting vs. Logic Change

One branch reformatted the file (prettier, gofmt, black), the other changed logic.

**Resolution**: Apply the logic change onto the reformatted version:
1. Accept the formatting side as base
2. Manually apply the logic changes from the other side
3. Run the formatter again to ensure consistency

### Pattern 2: Dependency Version Conflicts

Both branches updated the same dependency to different versions.

**Resolution**:
1. Check if versions are compatible (e.g., both are `^2.x`)
2. If not, pick the newer version and check for breaking changes
3. Update lock file accordingly
4. Run tests to verify compatibility

### Pattern 3: API Contract Divergence

Branch A changed a function signature; Branch B added a caller using the old signature.

**Resolution**:
1. Identify the new canonical signature
2. Update all call sites to match
3. Add a note in the commit about the breaking change
4. Consider adding a deprecation wrapper if this is a public API

### Pattern 4: Configuration File Drift

Both branches modified `.env.example`, `docker-compose.yml`, or similar config.

**Resolution**:
1. Merge additions from both sides
2. If the same key was set to different values, pick the correct one per environment
3. Document the decision in a comment if the choice is non-obvious

### Pattern 5: Overlapping Feature Branches

Two feature branches touch the same module for different features.

**Resolution**:
1. Map out which lines belong to Feature A vs. Feature B
2. Merge both sets of changes, ensuring they do not interfere
3. If they modify the same function for different purposes, refactor to separate concerns
4. Flag any coupling that should be addressed in a follow-up

## Anti-Patterns to Avoid

1. **Do NOT blindly accept "ours" or "theirs"** without reading both sides
2. **Do NOT leave conflict markers in the file** — even one `======` breaks compilation
3. **Do NOT resolve by concatenating both sides** — this creates duplicate or conflicting logic
4. **Do NOT skip test runs after resolving** — merged code may compile but behave incorrectly
5. **Do NOT force-push after a merge conflict resolution** on a shared branch without communicating
6. **Do NOT resolve binary conflicts by picking randomly** — compare the actual content
7. **Do NOT ignore rename conflicts** — they often indicate structural disagreements about the codebase

## Prevention Tips

When advising users on avoiding future conflicts:

- **Merge frequently**: Small, frequent merges reduce conflict scope
- **Communicate ownership**: Use CODEOWNERS to clarify who modifies which areas
- **Keep branches short-lived**: Long-lived branches accumulate more divergence
- **Use feature flags**: Decouple deployment from merging to reduce pressure on conflict resolution
- **Modularize code**: Smaller, focused files reduce the chance of overlapping edits
- **Auto-format on save**: Consistent formatting prevents whitespace-only conflicts

## Quick Reference Commands

```bash
# See all conflicted files
git diff --name-only --diff-filter=U

# See conflict details in a specific file
git diff <file>

# Show all 3 versions of a conflicted file
git show :1:<file>  # common ancestor
git show :2:<file>  # ours
git show :3:<file>  # theirs

# Abort a merge in progress
git merge --abort

# Abort a rebase in progress
git rebase --abort

# Retry merge with different strategy
git merge --abort && git merge <branch> -s recursive -X ours
```

## References

- **git-merge docs**: `git help merge` — merge strategies and options
- **git-rebase docs**: `git help rebase` — interactive rebase for conflict resolution
- **git-rerere**: `git config rerere.enabled true` — remember resolved conflicts for reuse
- **diff3 style**: `git config merge.conflictstyle diff3` — shows common ancestor in conflicts
