Created At: 2026-07-22T08:31:41Z
Completed At: 2026-07-22T08:31:41Z
File Path: `file:///c:/Users/ASUS/OneDrive/Documents/moodify/frontend/src/app/dashboard/profile/page.tsx`
Total Lines: 232
Total Bytes: 10033
Showing lines 1 to 232
The following code has been modified to include a line number before every line, in the format: <line_number>: <original_line>. Please note that any changes targeting the original code should remove the line number, colon, and leading space.
1: "use client";
2: 
3: import { useState, useEffect } from "react";
4: import { useTheme } from "next-themes";
5: import { useRouter } from "next/navigation";
6: import { User, Bell, Moon, Trash2, AlertTriangle, Loader2 } from "lucide-react";
7: import { toast } from "sonner";
8: import { Button } from "@/components/ui/button";
9: import { Switch } from "@/components/ui/switch";
10: import { createClient } from "@/lib/supabase/client";
11: import {
12:   AlertDialog,
13:   AlertDialogAction,
14:   AlertDialogCancel,
15:   AlertDialogContent,
16:   AlertDialogDescription,
17:   AlertDialogFooter,
18:   AlertDialogHeader,
19:   AlertDialogTitle,
20:   AlertDialogTrigger,
21: } from "@/components/ui/alert-dialog";
22: 
23: export default function ProfilePage() {
24:   const { theme, setTheme } = useTheme();
25:   const router = useRouter();
26:   const supabase = createClient();
27:   
28:   const [email, setEmail] = useState("");
29:   const [name, setName] = useState("");
30:   const [mounted, setMounted] = useState(false);
31:   const [isDeletingHistory, setIsDeletingHistory] = useState(false);
32:   const [isDeletingAccount, setIsDeletingAccount] = useState(false);
33:   
34:   // Stubs for preferences
35:   const [notificationsEnabled, setNotificationsEnabled] = useState(true);
36: 
37:   useEffect(() => {
38:     setMounted(true);
39:     const fetchUser = async () => {
40:       const { data: { user } } = await supabase.auth.getUser();
41:       if (user) {
42:         setEmail(user.email || "");
43:         setName(user.user_metadata?.name || "");
44:       }
45:     };
46:     fetchUser();
47:   }, [supabase.auth]);
48: 
49:   if (!mounted) return null;
50: 
51:   const handleSaveProfile = () => {
52:     // In a full app, this would update user_metadata in Supabase
53:     toast.success("Profile saved successfully");
54:   };
55: 
56:   const handleDeleteHistory = async () => {
57:     setIsDeletingHistory(true);
58:     try {
59:       const res = await fetch("/api/user/mood-history", { method: "DELETE" });
60:       if (!res.ok) throw new Error("Failed to delete");
61:       toast.success("Mood history deleted successfully.");
62:     } catch (err) {
63:       toast.error("Could not delete mood history.", { style: { backgroundColor: "var(--color-error)", color: "white" } });
64:     } finally {
65:       setIsDeletingHistory(false);
66:     }
67:   };
68: 
69:   const handleDeleteAccount = async () => {
70:     setIsDeletingAccount(true);
71:     try {
72:       const res = await fetch("/api/user/account", { method: "DELETE" });
73:       if (!res.ok) throw new Error("Failed to delete account");
74:       
75:       toast.success("Account deleted. We are sorry to see you go.");
76:       router.push("/login");
77:     } catch (err) {
78:       toast.error("Could not delete account. Please try again later.", { style: { backgroundColor: "var(--color-error)", color: "white" } });
79:       setIsDeletingAccount(false);
80:     }
81:   };
82: 
83:   return (
84:     <div className="w-full max-w-[800px] mx-auto py-8">
85:       <h1 className="text-h2 text-text-primary mb-8">Profile & Settings</h1>
86:       
87:       <div className="flex flex-col gap-8">
88:         
89:         {/* Personal Info */}
90:         <section className="bg-surface rounded-card border border-border p-6 shadow-small">
91:           <div className="flex items-center gap-3 mb-6">
92:             <User className="h-5 w-5 text-primary" />
93:             <h2 className="text-h4 text-text-primary">Personal Info</h2>
94:           </div>
95:           
96:           <div className="space-y-4 max-w-md">
97:             <div>
98:               <label className="block text-caption text-text-secondary font-semibold uppercase tracking-wider mb-2">Name</label>
99:               <input 
100:                 type="text" 
101:                 value={name} 
102:                 onChange={(e) => setName(e.target.value)}
103:                 placeholder="Your Name"
104:                 className="w-full bg-background border border-border rounded-input px-4 py-3 text-body focus:outline-none focus:ring-2 focus:ring-primary/30 transition-all"
105:               />
106:             </div>
107:             <div>
108:               <label className="block text-caption text-text-secondary font-semibold uppercase tracking-wider mb-2">Email Address</label>
109:               <input 
110:                 type="email" 
111:                 value={email} 
112:                 disabled
113:                 className="w-full bg-muted border border-border rounded-input px-4 py-3 text-body text-text-secondary opacity-70 cursor-not-allowed"
114:               />
115:             </div>
116:             <Button onClick={handleSaveProfile} className="rounded-button bg-primary text-white hover:bg-primary/90 shadow-small px-6 py-2">
117:               Save Changes
118:             </Button>
119:           </div>
120:         </section>
121: 
122:         {/* Preferences */}
123:         <section className="bg-surface rounded-card border border-border p-6 shadow-small">
124:           <div className="flex items-center gap-3 mb-6">
125:             <Bell className="h-5 w-5 text-primary" />
126:             <h2 className="text-h4 text-text-primary">Preferences</h2>
127:           </div>
128:           
129:           <div className="space-y-6">
130:             <div className="flex items-center justify-between">
131:               <div>
132:                 <h3 className="text-body font-medium text-text-primary">Dark Mode</h3>
133:                 <p className="text-caption text-text-secondary">Switch between light and dark themes</p>
134:               </div>
135:               <Switch 
136:                 checked={theme === "dark"}
137:                 onCheckedChange={(checked) => setTheme(checked ? "dark" : "light")}
138:               />
139:             </div>
140:             
141:             <div className="flex items-center justify-between">
142:               <div>
143:                 <h3 className="text-body font-medium text-text-primary">Push Notifications</h3>
144:                 <p className="text-caption text-text-secondary">Receive daily wellness reminders</p>
145:               </div>
146:               <Switch 
147:                 checked={notificationsEnabled}
148:                 onCheckedChange={setNotificationsEnabled}
149:               />
150:             </div>
151:           </div>
152:         </section>
153: 
154:         {/* Danger Zone */}
155:         <section className="bg-error/5 rounded-card border border-error/20 p-6 shadow-small mt-8">
156:           <div className="flex items-center gap-3 mb-6">
157:             <AlertTriangle className="h-5 w-5 text-error" />
158:             <h2 className="text-h4 text-error">Data & Privacy</h2>
159:           </div>
160:           
161:           <div className="space-y-6">
162:             <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-error/10">
163:               <div>
164:                 <h3 className="text-body font-medium text-text-primary">Delete Mood History</h3>
165:                 <p className="text-caption text-text-secondary">Permanently delete all your scans and chat logs.</p>
166:               </div>
167:               
168:               <AlertDialog>
169:                 <AlertDialogTrigger render={
170:                   <Button variant="outline" className="rounded-button border-error text-error hover:bg-error/10">
171:                     Delete History
172:                   </Button>
173:                 } />
174:                 <AlertDialogContent className="rounded-dialog max-w-md shadow-extra-large">
175:                   <AlertDialogHeader>
176:                     <AlertDialogTitle className="text-h3 text-text-primary">Are you sure?</AlertDialogTitle>
177:                     <AlertDialogDescription className="text-body text-text-secondary">
178:                       This will permanently delete your entire mood history, reports, and Lumi chat logs. This action cannot be undone.
179:                     </AlertDialogDescription>
180:                   </AlertDialogHeader>
181:                   <AlertDialogFooter className="mt-6">
182:                     <AlertDialogCancel autoFocus className="rounded-button border-border">Cancel</AlertDialogCancel>
183:                     <AlertDialogAction 
184:                       onClick={handleDeleteHistory}
185:                       className="rounded-button bg-error text-white hover:bg-error/90"
186:                     >
187:                       {isDeletingHistory ? <Loader2 className="h-4 w-4 animate-spin" /> : "Delete History"}
188:                     </AlertDialogAction>
189:                   </AlertDialogFooter>
190:                 </AlertDialogContent>
191:               </AlertDialog>
192:             </div>
193:             
194:             <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
195:               <div>
196:                 <h3 className="text-body font-medium text-text-primary">Delete Account</h3>
197:                 <p className="text-caption text-text-secondary">Permanently delete your account and all associated data.</p>
198:               </div>
199:               
200:               <AlertDialog>
201:                 <AlertDialogTrigger render={
202:                   <Button variant="destructive" className="rounded-button bg-error text-white hover:bg-error/90 shadow-small">
203:                     Delete Account
204:                   </Button>
205:                 } />
206:                 <AlertDialogContent className="rounded-dialog max-w-md shadow-extra-large">
207:                   <AlertDialogHeader>
208:                     <AlertDialogTitle className="text-h3 text-text-primary">Delete Account?</AlertDialogTitle>
209:                     <AlertDialogDescription className="text-body text-text-secondary">
210:                       This will permanently delete your account, wiping all personal info, scans, and settings from our servers. You cannot undo this.
211:                     </AlertDialogDescription>
212:                   </AlertDialogHeader>
213:                   <AlertDialogFooter className="mt-6">
214:                     <AlertDialogCancel autoFocus className="rounded-button border-border">Keep Account</AlertDialogCancel>
215:                     <AlertDialogAction 
216:                       onClick={handleDeleteAccount}
217:                       className="rounded-button bg-error text-white hover:bg-error/90"
218:                     >
219:                       {isDeletingAccount ? <Loader2 className="h-4 w-4 animate-spin" /> : "Delete Account"}
220:                     </AlertDialogAction>
221:                   </AlertDialogFooter>
222:                 </AlertDialogContent>
223:               </AlertDialog>
224:             </div>
225:           </div>
226:         </section>
227: 
228:       </div>
229:     </div>
230:   );
231: }
232: 
The above content shows the entire, complete file contents of the requested file.
