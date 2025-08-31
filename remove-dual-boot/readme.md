## Remove dual boot

### Pendrive delete partition

1. Plug in your pendrive.

2. Open **Command Prompt as Administrator**.

3. Type:

   ```bash
   diskpart
   ```

4. List all disks:

   ```bash
   list disk
   ```

   → Find your pendrive (likely 32 GB, e.g., `Disk 1`).

5. Select your pendrive:

   ```bash
   select disk X
   ```

   (replace **X** with your pendrive’s disk number, NOT your system disk — be careful!).

6. Clean the drive (this removes all partitions):

   ```bash
   clean
   ```

7. Create a new single partition:

   ```bash
   create partition primary
   ```

8. Format it (FAT32 or NTFS, depending on use):

   ```bash
   format fs=fat32 quick
   ```

   or

   ```bash
   format fs=ntfs quick
   ```

9. Assign a drive letter:

   ```bash
   assign
   ```

10. Exit:

    ```bash
    exit
    ```
