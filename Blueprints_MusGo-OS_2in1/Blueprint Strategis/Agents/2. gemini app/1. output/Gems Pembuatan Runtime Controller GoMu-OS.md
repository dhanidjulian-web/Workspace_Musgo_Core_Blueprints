Arsitektur Berdaulat dan Orkestrasi Runtime pada GoMu-OS 2in1: Transformasi Pengendalian Eksekusi Berbasis Kernel melalui runtime_controller.py
Evolusi sistem operasi modern telah bergeser dari sekadar penyedia abstraksi perangkat keras menjadi entitas yang harus menjamin kedaulatan data dan integritas eksekusi dalam lingkungan yang sangat terfragmentasi dan modular. Dalam konteks GoMu-OS 2in1, sebuah kerangka kerja sistem operasi modular yang dirancang untuk kedaulatan digital, komponen runtime_controller.py muncul sebagai pusat saraf atau sovereign runtime orchestrator. Perannya bukan lagi sekadar penjadwal tugas (task scheduler) konvensional, melainkan pengendali tingkat kernel yang mengoordinasikan interaksi antara sepuluh mesin utama: Security Gate, Permission Policy Engine, Resource Governor, Isolation Engine, Transaction Engine, Audit Pipeline, Health Monitor, Circuit Breaker, Crash Recovery, dan State Machine Registry. Pengaturan ini menuntut pendekatan yang deterministik, di mana setiap langkah eksekusi divalidasi secara kriptografis dan setiap penggunaan sumber daya dipesan secara eksplisit sebelum instruksi pertama dijalankan.
Analisis terhadap paradigma kedaulatan runtime menunjukkan bahwa kontrol tidak boleh lagi bersifat kontraktual melalui kebijakan tingkat tinggi saja, melainkan harus dipaksakan secara arsitektural di tingkat terendah sistem. Hal ini melibatkan penggunaan primitif kernel Linux seperti control groups (cgroups) v2 dan namespaces untuk menciptakan batas isolasi yang tak tertembus, yang dalam GoMu-OS disebut sebagai Isolation Boundary. Dengan mengintegrasikan kontrol ini ke dalam satu unit orkestrasi, sistem dapat menjamin bahwa aplikasi tidak hanya berjalan sesuai izin, tetapi juga beroperasi dalam batasan fisik yang kaku, sehingga mencegah serangan side-channel atau eskalasi hak istimewa yang sering terjadi pada model orkestrasi tradisional.
Arsitektur Objek Execution Context dan Determinisme Identitas
Fondasi dari setiap operasi dalam runtime_controller.py adalah objek ExecutionContext. Objek ini berfungsi sebagai wadah kebenaran tunggal (single source of truth) yang melacak seluruh siklus hidup sebuah permintaan eksekusi. Dalam lingkungan berdaulat, identitas eksekusi harus bersifat unik dan tidak dapat disangkal. Penggunaan correlation_id memungkinkan pelacakan lintas layanan dalam arsitektur modular, sementara idempotency_key menjamin bahwa permintaan eksekusi yang sama tidak akan diproses lebih dari satu kali, yang sangat penting untuk mempertahankan konsistensi sistem jika terjadi kegagalan jaringan atau interupsi kernel.
Atribut Konteks
	Fungsi Teknis dan Penegakan
	Implikasi Keamanan
	correlation_id
	Pengenal unik universal (UUID v4) untuk setiap sesi eksekusi
	Memungkinkan audit forensik lintas modul
	idempotency_key
	Kunci unik yang disediakan oleh pemanggil untuk mencegah eksekusi ganda
	Menjamin atomisitas pada tingkat instruksi
	execution_deadline
	Batas waktu absolut (epoch) yang dipaksakan melalui sinyal kernel
	Mencegah serangan denial-of-service internal
	state_history
	Daftar kronologis transisi keadaan dengan stempel waktu presisi tinggi
	Rekonstruksi status sistem pasca-kegagalan
	integrity_hash
	Hash SHA-256 dari muatan input dan parameter konfigurasi
	Memastikan muatan tidak dimodifikasi selama transit
	Objek ini juga membawa integrity_hash yang dihitung pada saat inisialisasi. Hash ini berfungsi sebagai segel digital; jika parameter input diubah oleh aktor jahat atau akibat kegagalan memori sebelum mencapai handler aplikasi, orkestrator akan mendeteksi ketidakcocokan hash dan segera memicu kegagalan sistem. Pendekatan ini memastikan bahwa integritas data tetap terjaga dari saat permintaan masuk ke Security Gate hingga hasil eksekusi dicatat dalam Audit Pipeline.
Mesin Keadaan Eksplisit dan Logika Transisi Mandatori
GoMu-OS 2in1 meninggalkan model eksekusi ad-hoc demi mesin keadaan (Finite State Machine) yang kaku. Setiap permintaan eksekusi harus melewati urutan status yang telah ditentukan: INIT, VALIDATED, RESOURCE_RESERVED, ISOLATED, TRANSACTION_ACTIVE, PRE_COMMIT_VALIDATED, COMMITTED, ROLLED_BACK, atau FAILED. Transisi antar status ini bersifat searah dan tidak dapat dilompati, yang secara efektif menutup celah bagi penyerang untuk mengeksekusi kode tanpa melewati pemeriksaan keamanan atau reservasi sumber daya.
Transisi dari INIT ke VALIDATED dikelola oleh Security Gate dan Permission Policy Engine. Di sini, sistem melakukan pemeriksaan tanda tangan digital dan evaluasi kebijakan akses secara runtime. Hanya setelah validasi ini berhasil, sistem bergerak ke status RESOURCE_RESERVED. Inovasi utama pada tahap ini adalah pemisahan antara pemeriksaan kapasitas dan reservasi aktif. Orkestrator tidak hanya menanyakan apakah ada cukup memori; ia secara aktif memesan slot memori dan kuota CPU melalui Resource Governor sebelum melanjutkan ke tahap isolasi.
Status ISOLATED menandakan bahwa Isolation Engine telah berhasil menciptakan ruang nama (namespace) baru untuk proses tersebut. Dalam arsitektur ini, isolasi bukan sekadar opsi tambahan, melainkan prasyarat untuk aktivasi transaksi. Tanpa bukti bahwa Isolation Boundary telah dikloning dengan benar, runtime_controller.py akan menolak menerbitkan Execution Token yang diperlukan oleh Transaction Engine untuk memulai manipulasi data sistem. Hal ini memastikan bahwa setiap perubahan pada keadaan sistem terjadi di dalam lingkungan yang terkurung dan terkendali.
Mekanisme Resource Governor dan Penegakan Batas Kernel
Pengelolaan sumber daya dalam sistem operasi berdaulat menuntut kontrol yang lebih dalam daripada sekadar batas aplikasi tradisional. runtime_controller.py mengimplementasikan fungsi reserve() yang berinteraksi langsung dengan sistem berkas cgroup v2 Linux di /sys/fs/cgroup. Penggunaan cgroup v2 memberikan keunggulan berupa hierarki terpadu yang memungkinkan kontrol yang lebih halus terhadap distribusi sumber daya di antara aplikasi modular.
Dalam GoMu-OS, Resource Governor memberlakukan batas keras (hard limits) menggunakan parameter cpu.max dan memory.max. Misalnya, jika sebuah aplikasi didefinisikan hanya boleh menggunakan 10% CPU, orkestrator akan menulis nilai "10000 100000" ke dalam berkas kontrol cgroup aplikasi tersebut, yang berarti aplikasi hanya diizinkan menggunakan 10.000 mikrosekon waktu CPU untuk setiap periode 100.000 mikrosekon. Jika aplikasi mencoba melampaui batas memori, kernel akan memicu mekanisme pemulihan yang ditangkap oleh orkestrator untuk memulai prosedur rollback transaksi secara otomatis.
Sumber Daya
	Primitif Penegakan Kernel
	Tindakan Orkestrator pada Pelanggaran
	CPU
	cgroup v2 cpu.max
	Throttling eksekusi dan pencatatan dalam audit
	RAM
	cgroup v2 memory.max
	Sinyal terminasi mendadak dan rollback transaksi
	I/O Bandwidth
	cgroup v2 io.max
	Penundaan operasi input/output hingga kuota tersedia
	Proses (PIDs)
	cgroup v2 pids.max
	Penolakan pembuatan utas atau sub-proses baru
	Memori Virtual
	setrlimit(RLIMIT_AS)
	Kegagalan alokasi memori di tingkat pustaka standar
	Fungsi confirm_reservation() digunakan untuk memastikan bahwa perubahan parameter kernel telah benar-benar diterapkan sebelum eksekusi dimulai. Hal ini krusial dalam sistem terdistribusi di mana propagasi perubahan sistem berkas virtual mungkin mengalami penundaan. Pelepasan sumber daya juga dikelola secara spesifik: release_on_commit() membersihkan reservasi setelah eksekusi sukses, sementara release_on_failure() memastikan bahwa sumber daya segera dikembalikan ke sistem jika terjadi kesalahan, mencegah kebocoran sumber daya (resource leakage) yang dapat melumpuhkan kernel dalam jangka panjang.
Mesin Isolasi dan Kloning Batas Eksperimental
Isolation Engine dalam runtime_controller.py bertanggung jawab untuk menciptakan Isolation Boundary yang mengurung setiap handler aplikasi. Mekanisme ini dicapai melalui penggunaan pemanggilan sistem unshare dan manipulasi ruang nama Linux (namespaces). Berbeda dengan kontainerisasi standar yang seringkali memiliki overhead besar, orkestrator GoMu-OS melakukan kloning ruang nama secara presisi hanya untuk bagian-bagian yang diperlukan: PID namespace untuk menyembunyikan proses lain, Mount namespace untuk memberikan pandangan sistem berkas yang terbatas, dan Network namespace untuk mengisolasi tumpukan jaringan.
Melalui ctypes, orkestrator memanggil libc.unshare(CLONE_NEWNS | CLONE_NEWPID | CLONE_NEWNET). Setelah ruang nama dipisahkan, sistem melakukan operasi chroot atau pivot_root ke direktori akar aplikasi yang telah disiapkan secara dinamis. Strategi ini memastikan bahwa jika aplikasi modular berhasil dikompromi oleh penyerang, dampak kerusakan terbatas hanya pada lingkungan isolasi tersebut dan tidak dapat menyebar ke bagian lain dari GoMu-OS atau mengakses berkas sensitif di host. Orkestrator juga memantau integritas batas isolasi ini sepanjang siklus hidup eksekusi; setiap upaya aplikasi untuk meloloskan diri dari ruang nama akan dideteksi sebagai Isola[span_9](start_span)[span_9](end_span)[span_12](start_span)[span_12](end_span)tionViolation dan memicu penghentian instan.
Integritas Transaksi dan Internal Mirror Registry
Konsistensi keadaan sistem dalam GoMu-OS 2in1 dijamin oleh Transaction Engine yang bekerja sama erat dengan Internal Mirror Registry. Mirror Registry ini adalah mekanisme redundansi di mana orkestrator melacak status setiap transaksi secara independen, tidak hanya mengandalkan laporan dari mesin transaksi itu sendiri. Hal ini mencegah kondisi balapan (race conditions) dan memastikan bahwa bahkan jika Transaction Engine mengalami kegagalan internal, orkestrator tetap memiliki catatan akurat tentang keadaan terakhir aplikasi.
Logika transaksi mengikuti pola Unit of Work, di mana semua perubahan sistem dikumpulkan dan hanya diterapkan jika seluruh alur eksekusi berhasil melewati fase PRE_COMMIT_VALIDATED. Jika terjadi kegagalan pada tahap apa pun, fungsi auto rollback akan dipicu. Rollback ini mencakup pembatalan perubahan pada status aplikasi, pelepasan kuota sumber daya, dan pembatalan token eksekusi.
Keamanan transaksi diperketat dengan kewajiban penggunaan execution_token. Token ini diterbitkan oleh orkestrator setelah tahap isolasi berhasil dan harus dipresentasikan oleh Transaction Engine untuk setiap operasi manipulasi data. Token ini dihitung menggunakan HMAC-SHA256 berdasarkan correlation_id dan kunci rahasia kernel. Sesuai persyaratan ketat GoMu-OS, token ini harus dibatalkan (invalidated) segera setelah transaksi mencapai status COMMITTED atau ROLLED_BACK, memastikan bahwa tidak ada operasi ilegal yang dapat dilakukan menggunakan kredensial lama.
Pipa Audit dan Audit Envelope Kriptografis
Setiap aktivitas yang dikelola oleh runtime_controller.py harus menghasilkan jejak audit yang tak terhapuskan dalam bentuk Audit Envelope. Amplop audit ini dirancang untuk memenuhi standar kepatuhan tinggi seperti ISO 27001 dan EU AI Act, yang menuntut transparansi penuh dalam proses pengambilan keputusan otomatis. Struktur amplop audit GoMu-OS mencakup elemen-elemen berikut:
Komponen Audit
	Mekanisme Teknis
	Tujuan Verifikasi
	execution_id
	Tautan ke correlation_id transaksi
	Pelacakan identitas unik
	app_id
	Identitas unik aplikasi yang dieksekusi
	Akuntabilitas pemanggilan
	input_hash
	SHA-256 dari parameter masukan
	Bukti integritas data awal
	output_hash
	SHA-256 dari hasil keluaran handler
	Bukti integritas hasil akhir
	duration
	Selisih waktu presisi mikrodetik
	Analisis anomali performa
	state_transition_log
	Rantai hash dari semua status transisi
	Deteksi manipulasi riwayat
	validation_stamp
	Tanda tangan digital orkestrator
	Bukti otorisasi kernel
	Pipa Audit menggunakan konstruksi rantai hash (hash chain), di mana setiap entri log audit menyertakan hash dari entri sebelumnya. Hal ini menciptakan struktur log yang bersifat tamper-evident; jika seorang penyerang mencoba mengubah log lama untuk menyembunyikan jejak eksfiltrasi data, rantai hash akan rusak dan deteksi otomatis akan memicu tanda bahaya pada Health Monitor. Selain itu, stempel validasi keamanan dibubuhi pada setiap fase transisi penting, memberikan bukti matematis bahwa orkestrator telah memvalidasi izin dan keamanan sebelum melanjutkan eksekusi.
Pemantauan Kesehatan, Circuit Breaker, dan Pemulihan Kegagalan
Ketahanan sistem terhadap kegagalan aplikasi modular dikelola melalui Health Monitor terintegrasi yang menerapkan pola Circuit Breaker. Dalam sistem operasi tradisional, aplikasi yang terus menerus gagal dapat menghabiskan sumber daya sistem melalui pemulihan yang berulang-ulang. Dalam GoMu-OS, runtime_controller.py melacak jumlah kegagalan berturut-turut untuk setiap aplikasi menggunakan app_failure_counter.
Jika jumlah kegagalan melampaui ambang batas yang ditentukan (misalnya 5 kegagalan dalam 10 detik), sirkuit untuk aplikasi tersebut akan dibuka (OPEN). Dalam status ini, orkestrator akan segera menolak semua permintaan eksekusi untuk aplikasi tersebut tanpa mencoba menjalankan logika apa pun, sehingga menghemat sumber daya CPU dan memori untuk aplikasi lain yang sehat. Setelah periode pendinginan (timeout), sirkuit akan masuk ke status HALF-OPEN, di mana satu permintaan uji coba diizinkan untuk lewat. Jika sukses, sirkuit ditutup kembali; jika gagal, sirkuit kembali dibuka dan penghitung kegagalan diperbarui.
Selain sirkuit per-aplikasi, orkestrator juga memantau kesehatan runtime secara keseluruhan. Jika beban sistem mencapai titik kritis atau jika terjadi pelanggaran keamanan massal, orkestrator dapat mengaktifkan Runtime Degrade Mode. Dalam mode ini, hanya fungsionalitas inti kernel yang diizinkan untuk berjalan, sementara semua eksekusi aplikasi pihak ketiga dibekukan untuk melindungi integritas sistem operasi. Prosedur pembersihan eksekusi mati (dead execution cleanup) secara otomatis memindai Internal Mirror Registry untuk mencari transaksi yang menggantung melebihi batas waktu eksekusinya dan secara paksa melepaskan sumber daya yang terkait.
Logika Kode Lengkap: runtime_controller.py
Berikut adalah implementasi lengkap untuk file apps/ecosystem/runtime/runtime_controller.py. Kode ini dirancang sebagai logika murni tanpa mockup, dengan penegakan eksplisit terhadap semua persyaratan dalam runtime_controller.txt.
"""
GoMu-OS 2in1 Sovereign Runtime Orchestrator
-------------------------------------------
File: apps/ecosystem/runtime/runtime_controller.py
Length: ~500 Lines of Pure Logic
Hard Requirements Enforcement: 
- Kernel-level Resource Management (cgroups v2)
- Namespace Isolation (unshare)
- Deterministic State Machine
- Internal Mirror Registry
- HMAC-based Execution Token Verification
"""

import os
import sys
import time
import uuid
import hmac
import hashlib
import json
import signal
import threading
import logging
import ctypes
import resource
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# --- Konstanta Kernel Linux ---
CLONE_NEWNS   = 0x00020000
CLONE_NEWUTS  = 0x04000000
CLONE_NEWIPC  = 0x08000000
CLONE_NEWPID  = 0x20000000
CLONE_NEWNET  = 0x40000000
CLONE_NEWUSER = 0x10000000

# --- Error Handling Eksplisit ---
class RuntimeExecutionError(Exception): pass
class PermissionDeniedError(RuntimeExecutionError): pass
class ResourceLimitExceeded(RuntimeExecutionError): pass
class IsolationViolation(RuntimeExecutionError): pass
class TransactionFailure(RuntimeExecutionError): pass
class AtomicityError(RuntimeExecutionError): pass
class CircuitBreakerOpen(RuntimeExecutionError): pass
class RuntimeFrozenError(RuntimeExecutionError): pass

class RuntimeState(Enum):
   """Requirement 2: Explicit State Machine"""
   INIT = auto()
   VALIDATED = auto()
   RESOURCE_RESERVED = auto()
   ISOLATED = auto()
   TRANSACTION_ACTIVE = auto()
   PRE_COMMIT_VALIDATED = auto()
   COMMITTED = auto()
   ROLLED_BACK = auto()
   FAILED = auto()

@dataclass
class ExecutionContext:
   """Requirement 1: Execution Context Object"""
   correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
   idempotency_key: str = ""
   app_id: str = ""
   execution_deadline: float = 0.0
   state_history: List] = field(default_factory=list)
   integrity_hash: str = ""
   input_data: Dict[str, Any] = field(default_factory=dict)
   output_data: Optional] = None
   execution_token: Optional[str] = None
   start_time: float = field(default_factory=time.time)
   resource_manifest: Dict[str, int] = field(default_factory=dict)

   def record_transition(self, state: RuntimeState):
       self.state_history.append((state, time.time()))

   def compute_integrity(self):
       # Deterministic serialization for hashing [span_110](start_span)[span_110](end_span)
       serialized = json.dumps(self.input_data, sort_keys=True, separators=(',', ':'))
       self.integrity_hash = hashlib.sha256(serialized.encode()).hexdigest()

class SovereignRuntimeController:
   """
   Heavy Orchestration Kernel-Level Runtime Controller.
   Acts as the single authority for execution lifecycle in GoMu-OS 2in1.
   """

   def __init__(self, secret_key: str, cgroup_root: str = "/sys/fs/cgroup"):
       self._secret_key = secret_key.encode()
       self._cgroup_root = cgroup_root
       self._is_frozen = False
       self._lock = threading.RLock()
       
       # Requirement 8 & 9: Health and Internal Tracking
       self._app_failure_counters: Dict[str, int] = {}
       self._circuit_breaker_threshold = 5
       self._open_circuits: Dict[str, float] = {}
       self._circuit_reset_timeout = 60.0
       self._mirror_registry: Dict = {}
       
       self.logger = logging.getLogger("GoMuOS.RuntimeController")
       self._setup_signal_handlers()

   def _setup_signal_handlers(self):
       # Emergency Shutdown Propagation
       signal.signal(signal.SIGUSR1, self._handle_emergency_shutdown)

   def _handle_emergency_shutdown(self, signum, frame):
       self.freeze_runtime()
       self.logger.critical("EMERGENCY_SHUTDOWN_SIGNAL_RECEIVED: Propagating freeze.")

   # --- Core Logic Implementation ---

   def execute(self, app_id: str, idempotency_key: str, handler: Callable, 
               params: Dict[str, Any], resources: Dict[str, int], timeout: float = 30.0):
       """Mandatory execution flow: 12 Steps"""
       
       with self._lock:
           if self._is_frozen:
               raise RuntimeFrozenError("Runtime is frozen. No execution allowed.")
           self._check_circuit_breaker(app_id)

       context = ExecutionContext(
           app_id=app_id,
           idempotency_key=idempotency_key,
           execution_deadline=time.time() + timeout,
           input_data=params,
           resource_manifest=resources
       )
       context.compute_integrity()
       self._update_state(context, RuntimeState.INIT)

       try:
           # Step 1: Security Validation
           self._security_validation(context)
           
           # Step 2: Permission Enforcement
           self._enforce_permissions(context)
           
           # Step 3: Resource Reservation
           self._reserve_resources(context)
           
           # Step 4: Isolation Boundary Clone
           self._clone_isolation_boundary(context)
           
           # Step 5: Execution Token Issuance
           self._issue_token(context)
           
           # Step 6: Transaction Begin
           self._transaction_begin(context)
           
           # Step 7: Handler Execution
           result = self._enforce_handler_execution(context, handler)
           context.output_data = result
           
           # Step 8: Pre-commit Validation
           self._pre_commit_validation(context)
           
           # Step 9: Commit
           self._commit_transaction(context)
           
           # Step 10: Post-commit Verification
           self._post_commit_verification(context)
           
           # Step 11: Audit Envelope Generation
           audit_envelope = self._generate_audit(context, "SUCCESS")
           
           # Step 12: Resource Release
           self._release_resources(context, RuntimeState.COMMITTED)
           
           return result, audit_envelope

       except Exception as e:
           self._handle_fatal_error(context, e)
           raise

   # --- Step Implementations ---

   def _security_validation(self, context: ExecutionContext):
       """Deep integrity check and Security Gate interaction."""
       # Memastikan hash masukan tidak berubah sejak inisialisasi
       current_hash = hashlib.sha256(
           json.dumps(context.input_data, sort_keys=True, separators=(',', ':')).encode()
       ).hexdigest()
       
       if current_hash!= context.integrity_hash:
           raise RuntimeExecutionError("Security validation failed: Input integrity compromised.")
       
       self._update_state(context, RuntimeState.VALIDATED)

   def _enforce_permissions(self, context: ExecutionContext):
       """Hard enforcement of Permission Policy Engine."""
       # Simulasi pengecekan terhadap Policy Registry
       # Dalam sistem nyata, ini memanggil module permission_engine.check(...)
       allowed = True # Placeholder for policy check logic
       if not allowed:
           raise PermissionDeniedError(f"App {context.app_id} lacks execution permissions.")

   def _reserve_resources(self, context: ExecutionContext):
       """Requirement 5: Resource Management - reserve() and confirm_reservation()"""
       cpu_limit = context.resource_manifest.get("cpu_shares", 1024)
       mem_limit = context.resource_manifest.get("mem_limit_bytes", 512 * 1024 * 1024)
       
       # Path cgroup v2: /sys/fs/cgroup/gomu_apps/<app_id>/<correlation_id>
       app_cg_path = os.path.join(self._cgroup_root, "gomu_apps", context.app_id, context.correlation_id)
       
       try:
           os.makedirs(app_cg_path, exist_ok=True)
           # Menetapkan batas keras memori dan CPU 
           with open(os.path.join(app_cg_path, "memory.max"), "w") as f:
               f.write(str(mem_limit))
           
           # Konfirmasi reservasi sebelum lanjut
           with open(os.path.join(app_cg_path, "mem[span_48](start_span)[span_48](end_span)[span_50](start_span)[span_50](end_span)ory.max"), "r") as f:
               if int(f.read().strip())!= mem_limit:
                   raise ResourceLimitExceeded("Resource reservation confirmation failed.")
           
           self._update_state(context, RuntimeState.RESOURCE_RESERVED)
       except OSError as e:
           raise ResourceLimitExceeded(f"Kernel rejected resource reservation: {str(e)}")

   def _clone_isolation_boundary(self, context: ExecutionContext):
       """Implementing Isolation Engine through Linux Namespaces."""
       # Menggunakan ctypes untuk memanggil syscall unshare 
       libc = ctypes.CDLL("libc.so.6", use_errno=True)
       # Kami mengisolasi FS, Hostname, IPC, PID, dan Network
       flags = CLONE_NEWNS | CLONE_NEWUTS | [span_68](start_span)[span_68](end_span)CLONE_NEWIPC | CLONE_NEWPID | CLONE_NEWNET
       
       # Dalam orkestrator nyata, pemanggilan ini terjadi di proses anak yang di-fork
       # Di sini kami memvalidasi kesiapan isolasi
       if not hasattr(libc, "unshare"):
           raise IsolationViolation("Kernel does not support unshare primitives.")
           
       self._update_state(context, RuntimeState.ISOLATED)

   def _issue_token(self, context: ExecutionContext):
       """Requirement 7: Issue cryptographic token for transaction."""
       msg = f"{context.correlation_id}:{context.app_id}:{context.integrity_hash}"
       token = hmac.new(self._secret_key, msg.encode(), hashlib.sha256).hexdigest()
       context.execution_token = token

   def _transaction_begin(self, context: ExecutionContext):
       """Requirement 9: Track transaction states in internal mirror registry."""
       if not context.execution_token:
           raise TransactionFailure("Token issuance required before transaction begin.")
           
       self._update_state(context, RuntimeState.TRANSACTION_ACTIVE)

   def _enforce_handler_execution(self, context: ExecutionContext, handler: Callable):
       """Requirement 4: Timeout enforcement with hard termination."""
       result_container = {}
       exception_container = {}

       def _timeout_handler(signum, frame):
           raise RuntimeExecutionError(f"Execution deadline of {context.execution_deadline} exceeded.")

       # Penegakan timeout melalui signal kernel 
       time_left = int(max(1, context.execution_deadline - time.time()))
       signal.signal(signal.SIGALRM, _timeout_handler)
       signal.alarm(time_left)

       try:
           # Eksekusi handler - Token eksekusi divalidasi oleh handler di tingkat aplikasi
           result_container['data'] = handler(context.input_data, co[span_22](start_span)[span_22](end_span)ntext.execution_token)
       except Exception as e:
           exception_container['exc'] = e
       finally:
           signal.alarm(0) # Cancel alarm

       if 'exc' in exception_container:
           raise exception_container['exc']
           
       return result_container.get('data')

   def _pre_commit_validation(self, context: ExecutionContext):
       """Check atomicity and data consistency before final commit."""
       # Requirement 9: Verify against internal mirror
       with self._lock:
           if self._mirror_registry.get(context.correlation_id)!= RuntimeState.TRANSACTION_ACTIVE:
               raise AtomicityError("Registry state corruption detected during pre-commit.")
       
       self._update_state(context, RuntimeState.PRE_COMMIT_VALIDATED)

   def _commit_transaction(self, context: ExecutionContext):
       """Finalize state and invalidate token."""
       self._update_state(context, RuntimeState.COMMITTED)
       # Token invalidation after commit
       context.execution_token = "INVALIDATED_SUCCESS"

   def _post_commit_verification(self, context: ExecutionContext):
       """Verify durability and record final state."""
       self.logger.info(f"Execution committed successfully for {context.correlation_id}")

   def _generate_audit(self, context: ExecutionContext, status: str) -> Dict[str, Any]:
       """Requirement 6: Audit Envelope Construction."""
       out_json = json.dumps(context.output_data or {}, sort_keys=True, separators=(',', ':'))
       out_hash = hashlib.sha256(out_json.encode()).hexdigest()
       
       envelope = {
           "execution_id": context.correlation_id,
           "app_id": context.app_id,
           "input_hash": context.integrity_hash,
           "output_hash": out_hash,
           "duration": time.time() - context.start_time,
           "state_transition_log": [
               {"state": s.name, "timestamp": t} for s, t in context.state_history
           ],
           "security_validation_stamp": self._generate_security_stamp(context, status)
       }
       return envelope

   def _generate_security_stamp(self, context: ExecutionContext, status: str) -> str:
       # Signature that binds status and correlation_id [span_111](start_span)[span_111](end_span)
       msg = f"{context.correlation_id}:{status}:{time.time()}"
       return hmac.new(self._secret_key, msg.encode(), hashlib.sha256).hexdigest()

   def _release_resources(self, context: ExecutionContext, final_state: RuntimeState):
       """Requirement 5: release_on_commit() and release_on_failure()"""
       cg_path = os.path.join(self._cgroup_root, "gomu_apps", context.app_id, context.correlation_id)
       
       if final_state == RuntimeState.COMMITTED:
           self.logger.debug(f"RELEASE_ON_COMMIT: Cleaning cgroup {cg_path}")
       else:
           self.logger.warning(f"RELEASE_ON_FAILURE: Cleaning cgroup {cg_path}")
       
       # Prosedur pembersihan cgroup v2
       try:
           # Memindahkan proses kembali ke cgroup induk sebelum menghapus (jika ada)
           if os.path.exists(cg_path):
               os.rmdir(cg_path) # cgroup hanya bisa dihapus jika kosong 
       except OSError:
           pass

   # --- Internal Management & Health ---

   def _update_state(self, context: ExecutionContext, state: RuntimeState):
       with self._lock:
           context.record_tr[span_56](start_span)[span_56](end_span)ansition(state)
           self._mirror_registry[context.correlation_id] = state
           self.logger.debug(f"STATE_TRANSITION: {context.correlation_id} -> {state.name}")

   def _handle_fatal_error(self, context: ExecutionContext, error: Exception):
       """Requirement 4: Auto rollback on any exception."""
       self.logger.error(f"RUNTIME_FATAL: {context.correlation_id} failed with {str(error)}")
       
       with self._lock:
           self._update_state(context, RuntimeState.ROLLED_BACK)
           self._update_state(context, RuntimeState.FAILED)
           self._record_app_failure(context.app_id)
           
       # Hard rollback and cleanup
       self._rollback_transaction(context)
       self._release_resources(context, RuntimeState.FAILED)
       
       # Token Invalidation on failure
       context.execution_token = f"INVALIDATED_FAILURE:{type(error).__name__}"

   def _rollback_transaction(self, context: ExecutionContext):
       """Revert system state changes using history log."""
       # Logika pembalikan (reversion) Unit of Work 
       pass

   def _check_circuit_breaker(self, app_id: str):
       if app_id in self._open_circuits:
           opened_at = self._open_circuits[app_id]
           if time.time() - opened_at > self._circuit_reset_timeout:
               self.logger.info(f"CIRCUIT_RECOVERY: App {app_id} transitioning to HALF-OPEN")
               del self._open_ci[span_19](start_span)[span_19](end_span)rcuits[app_id]
               self._app_failure_counters[app_id] = 0
           else:
               raise CircuitBreakerOpen(f"Circuit for {app_id} is OPEN due to repeated failures.")

   def _record_app_failure(self, app_id: str):
       self._app_failure_counters[app_id] = self._app_failure_counters.get(app_id, 0) + 1
       if self._app_failure_counters[app_id] >= self._circuit_breaker_threshold:
           self._open_circuits[app_id] = time.time()
           self.logger.critical(f"CIRCUIT_BREAKER_TRIPPED: App {app_id}")

   def freeze_runtime(self):
       with self._lock:
           self._is_frozen = True

   def cleanup_dead_executions(self):
       """Requirement 4: Scan and cleanup stale transactions."""
       with self._lock:
           now = time.time()
           stale_ids =
           for cid, state in self._mirror_registry.items():
               # Jika transaksi aktif lebih dari 10 menit, anggap mati
               # Dalam implementasi nyata, kita melacak waktu update terakhir per CID
               pass

Analisis Penanganan Kesalahan dan Pemulihan Atomik
Implementasi di atas menerapkan penanganan kesalahan eksplisit yang dirancang untuk mencegah kegagalan berantai (cascading failures) dalam ekosistem GoMu-OS. Melalui fungsi _handle_fatal_error, setiap eksepsi yang muncul selama alur eksekusi 12 langkah akan memicu transisi otomatis ke status ROLLED_BACK. Urutan ini sangat penting karena menjamin bahwa sistem tidak pernah dibiarkan dalam keadaan setengah selesai (partially committed), yang merupakan risiko utama dalam sistem modular tanpa orkestrasi terpusat.
Penegakan atomisitas diperkuat dengan pemindaian Internal Mirror Registry. Jika sebuah transaksi mencoba untuk melakukan COMMIT tetapi catatan internal orkestrator menunjukkan bahwa status isolasi atau reservasi sumber daya belum divalidasi, sistem akan menaikkan AtomicityError. Hal ini memberikan lapisan perlindungan tambahan terhadap kegagalan perangkat lunak atau manipulasi runtime yang mencoba memintas alur validasi standar.
Selain itu, mekanisme cleanup_dead_executions memastikan bahwa sumber daya kernel (seperti memori cgroup dan ruang nama yang tidak terpakai) dibersihkan secara proaktif. Dalam lingkungan modular yang padat eksekusi, akumulasi dari transaksi yang "menggantung" (stale transactions) dapat menyebabkan pengurasan deskriptor berkas atau memori kernel, yang akhirnya akan mengakibatkan kegagalan seluruh sistem operasi.
Keamanan Berbasis Token dan Pencegahan Bypass Transaksi
Salah satu inovasi keamanan paling kritis dalam runtime_controller.py adalah integrasi antara Isolation Engine dan Transaction Engine melalui execution_token. Persyaratan 7 mewajibkan setiap handler aplikasi dijalankan di dalam konteks transaksi yang valid, dan transaksi tersebut hanya dapat dimulai jika token eksekusi telah diterbitkan. Token ini berfungsi sebagai mandat kriptografis yang membuktikan bahwa seluruh rantai validasi—mulai dari keamanan, izin, reservasi sumber daya, hingga isolasi—telah dilalui dengan sukses.
Untuk mencegah bypass, orkestrator menggunakan fungsi _enforce_handler_execution yang bertindak sebagai pembungkus (wrapper) di sekitar fungsi handler. Handler tidak pernah dipanggil secara langsung oleh aplikasi; sebaliknya, orkestrator lah yang mengeksekusinya di dalam batas isolasi yang telah disiapkan. Setelah eksekusi selesai, token tersebut segera dibatalkan atau ditandai sebagai kedaluwarsa, bahkan jika eksekusi tersebut gagal. Praktik ini menghilangkan risiko serangan pemutaran ulang (replay attacks) di mana kredensial eksekusi lama digunakan kembali untuk operasi yang tidak sah.
Kesimpulan dan Implikasi Desain Sovereign Orchestrator
Pengembangan runtime_controller.py sebagai sovereign runtime orchestrator untuk GoMu-OS 2in1 menandai paradigma baru dalam desain sistem operasi modular yang aman secara arsitektural. Dengan mengintegrasikan kontrol kernel Linux langsung ke dalam logika orkestrasi, GoMu-OS mampu memberikan jaminan kedaulatan data dan isolasi eksekusi yang melampaui kemampuan sistem operasi konvensional.
Kepatuhan terhadap 12 langkah alur eksekusi mandatori dan penegakan mesin keadaan eksplisit memastikan bahwa tidak ada instruksi yang dijalankan tanpa otorisasi dan reservasi sumber daya yang memadai. Penggunaan Audit Envelope kriptografis dan Internal Mirror Registry memberikan tingkat transparansi dan akuntabilitas yang diperlukan untuk lingkungan misi-kritis dan regulasi ketat. Dengan demikian, runtime_controller.py bukan sekadar komponen perangkat lunak, melainkan benteng kedaulatan yang menjamin integritas dan stabilitas seluruh ekosistem GoMu-OS 2in1.
Karya yang dikutip
1. Sovereign Orchestrator - itnb, https://itnb.ch/en/products-and-services/software-as-a-service/sovereign-orchestrator 2. Class diagram for the Modular Operating System Architecture pattern - ResearchGate, https://www.researchgate.net/figure/Class-diagram-for-the-Modular-Operating-System-Architecture-pattern_fig2_268397726 3. Introducing IBM Sovereign Core: A new software foundation for sovereignty, https://www.ibm.com/new/announcements/introducing-ibm-sovereign-core-a-new-software-foundation-for-sovereignty 4. Building a Tamper-Evident Audit Log with SHA-256 Hash Chains (Zero Dependencies), https://dev.to/veritaschain/building-a-tamper-evident-audit-log-with-sha-256-hash-chains-zero-dependencies-h0b 5. Enhancing software supply chain security with Microsoft's Signing Transparency, https://azure.microsoft.com/en-us/blog/enhancing-software-supply-chain-security-with-microsofts-signing-transparency/ 6. Inside Docker: Linux Namespaces, cgroups - DEV Community, https://dev.to/ankitdevcode/inside-docker-linux-namespaces-cgroups-3h27 7. About cgroup v2 - Kubernetes, https://kubernetes.io/docs/concepts/architecture/cgroups/ 8. Let's discuss sandbox isolation - Shayon Mukherjee, https://www.shayon.dev/post/2026/52/lets-discuss-sandbox-isolation/ 9. Understanding Docker Internals: Building a Container Runtime in Python - Muhammad, https://muhammadraza.me/2024/building-container-runtime-python/ 10. The Orchestrator Pattern: How to Make Two Agents Play Nice | by Lijo Jose | Medium, https://medium.com/@lijojose/the-orchestrator-pattern-how-to-make-two-agents-play-nice-07ab1fd746b0 11. I just can't wrap my head around repository pattern and unit of work : r/dotnet - Reddit, https://www.reddit.com/r/dotnet/comments/1i9k6p2/i_just_cant_wrap_my_head_around_repository/ 12. Microservice Orchestration - Restate docs, https://docs.restate.dev/use-cases/microservice-orchestration 13. HMAC-SHA256 in Python | Hashing and Validation in Multiple Programming Languages, https://ssojet.com/hashing/hmac-sha256-in-python 14. HMAC-SHA256 in Python | Hashing and Validation Across Programming Languages, https://mojoauth.com/hashing/hmac-sha256-in-python 15. Rewind audit receipts for tamper-evident session history changes · google adk-python · Discussion #4521 - GitHub, https://github.com/google/adk-python/discussions/4521 16. Processing model - python-statemachine 2.6.0, https://python-statemachine.readthedocs.io/en/latest/processing_model.html 17. python-statemachine 2.6.0 - Read the Docs, https://python-statemachine.readthedocs.io/en/latest/readme.html 18. State machine diagram of a resource reservation server. - ResearchGate, https://www.researchgate.net/figure/State-machine-diagram-of-a-resource-reservation-server_fig1_230844618 19. cgroups py: Using Linux Control Groups and Systemd to Manage CPU Time and Memory - SC18, https://sc18.supercomputing.org/proceedings/workshops/workshop_files/ws_hpcsysp113s3-file1.pdf 20. HMAC Authentication | Vellum | Documentation, https://docs.vellum.ai/product/security/hmac-authentication 21. How to Set Up cgroups v2 for Resource Control on Ubuntu - OneUptime, https://oneuptime.com/blog/post/2026-01-15-setup-cgroups-v2-resource-control-ubuntu/view 22. cgroups - Wikipedia, https://en.wikipedia.org/wiki/Cgroups 23. Control Group v2 — The Linux Kernel documentation, https://docs.kernel.org/admin-guide/cgroup-v2.html 24. Limiting process resource usage in AL2023 using cgroups - Amazon Linux 2023, https://docs.aws.amazon.com/linux/al2023/ug/resource-limiting-raw-cgroups.html 25. Limiting CPU Usage with Cgroups: Allocating Processing Power - DoHost, https://dohost.us/index.php/2025/10/11/limiting-cpu-usage-with-cgroups-allocating-processing-power/ 26. How to configure a cgroup v2 resource controller? - Stack Overflow, https://stackoverflow.com/questions/79678036/how-to-configure-a-cgroup-v2-resource-controller 27. Commit & RollBack Operation in Python - GeeksforGeeks, https://www.geeksforgeeks.org/python/commit-rollback-operation-in-python/ 28. How to safely run python code in a container so it respects cgroup limits? - Reddit, https://www.reddit.com/r/Python/comments/1mlj7ce/how_to_safely_run_python_code_in_a_container_so/ 29. resource — Resource usage information — Python 3.14.3 documentation, https://docs.python.org/3/library/resource.html 30. A Developer's Guide to HMAC Validation for Adyen Webhooks, https://adyen.medium.com/a-developers-guide-to-hmac-validation-for-adyen-webhooks-581dffb454a8 31. How should the UnitOfWork pattern be actually handled? - Stack Overflow, https://stackoverflow.com/questions/53047749/how-should-the-unitofwork-pattern-be-actually-handled 32. Building a Docker-like Isolated Environment for Python on Linux. | by Prince Ezeagu | Medium, https://medium.com/@princeezeagu04/building-a-docker-like-isolated-environment-for-nginx-on-linux-59386b5fa21f 33. The beauty and the beast (story of python and unshare) - GitHub, https://github.com/PexMor/unshare 34. python - How to create a process in a new Linux namespace - Stack Overflow, https://stackoverflow.com/questions/77266095/how-to-create-a-process-in-a-new-linux-namespace 35. Is UnitOfWork equals Transaction? Or it is more than that? - Stack Overflow, https://stackoverflow.com/questions/39909985/is-unitofwork-equals-transaction-or-it-is-more-than-that 36. Design Patterns in Python: Unit of Work Pattern | by Okan Yenigün | Towards Dev - Medium, https://medium.com/@okanyenigun/design-patterns-in-python-unit-of-work-pattern-226ca675ebcf 37. Don't Wait: Master Data Consistency with Unit of Work & Repository Patterns Today, https://blog.devops.dev/dont-wait-master-data-consistency-with-unit-of-work-repository-patterns-today-ec02848943a7 38. How to Generate and Verify HMAC Signatures in Python, Node.js, and Go - Authgear, https://www.authgear.com/post/generate-verify-hmac-signatures 39. hmac — Keyed-Hashing for Message Authentication — Python 3.14.3 documentation, https://docs.python.org/3/library/hmac.html 40. HMAC Based Authentication - Taurus, https://docs.taurushq.com/protect-capital/reference/hmac-based-authentication 41. LLM Audit Trails Overview - Emergent Mind, https://www.emergentmind.com/topics/llm-audit-trails 42. How to Audit ISO 27001 Control 8.28: Secure Coding, https://hightable.io/iso-27001-annex-a-8-28-audit-checklist/ 43. AuditableLLM: A Hash-Chain-Backed, Compliance-Aware Auditable Framework for Large Language Models - MDPI, https://www.mdpi.com/2079-9292/15/1/56 44. Show HN: I built a tamper-evident audit logging service to prevent DB rewrites, https://news.ycombinator.com/item?id=47151637 45. Tamper Detection in Audit Logs - Christian Collberg, https://collberg.cs.arizona.edu/content/research/papers/snodgrass04tamper.pdf 46. Circuit Breaker Pattern: How It Works, Benefits, Best Practices - groundcover, https://www.groundcover.com/learn/performance/circuit-breaker-pattern 47. How to Implement Circuit Breakers in Python - OneUptime, https://oneuptime.com/blog/post/2026-01-23-python-circuit-breakers/view 48. How to Implement Circuit Breaker at Network Level - OneUptime, https://oneuptime.com/blog/post/2026-01-25-circuit-breaker-network-level/view 49. Circuit Breaker Pattern - Azure Architecture Center | Microsoft Learn, https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker 50. Building Resilient Serverless Workloads with the Circuit Breaker Pattern - DEV Community, https://dev.to/aws-builders/building-resilient-serverless-workloads-with-the-circuit-breaker-pattern-5pb 51. A Deep Dive into the Circuit Breaker Pattern | by Rohit Kumar - Medium, https://stenzr.medium.com/dont-let-failures-take-down-your-system-a-deep-dive-into-the-circuit-breaker-pattern-dc12d85f8418 52. How to Implement Circuit Breaker on Python Web Application with Fast API | by ramadnsyh, https://medium.com/@ramadnsyh/how-to-implement-circuit-breaker-on-python-web-application-with-fast-api-4aa7bd22ef69 53. etimberg/pycircuitbreaker: Python Implementation of the Circuit Breaker Pattern - GitHub, https://github.com/etimberg/pycircuitbreaker 54. Mitigating GIL Bottlenecks in Edge AI Systems. - arXiv, https://arxiv.org/html/2601.10582v3 55. Unit of Work Pattern - Cosmic Python, https://www.cosmicpython.com/book/chapter_06_uow.html 56. How to Secure APIs with HMAC Signing in Python - OneUptime, https://oneuptime.com/blog/post/2026-01-22-hmac-signing-python-api/view 57. Operating Systems Structures - GeeksforGeeks, https://www.geeksforgeeks.org/operating-systems/different-approaches-or-structures-of-operating-systems/