# WhatsApp Outreach Messages for Gaby — 6 templates by play

Source: pre-built from `paragu-ai-leads` dataset scoring. Total contact list: see `gaby-outreach-pack.csv`. Use the `outreach_template` column to pick which message.

---

## 1. DENTAL_COLLEAGUE (use for "DIRECT_DENTAL" play — peer referral, not competitor)

> Hola [NOMBRE], soy Dra. Gabriella González Pane, odontóloga conservadora en Mburucuyá (Asunción) — 20+ años de práctica, foco en rehabilitación oral + segunda opinión escrita. Vi que [NOMBRE_CLÍNICA] tiene [N] reseñas en Google. ¿Tenés 15 min para un café y hablamos de posibles derivaciones entre colegas? Trabajo casos complejos de rehabilitación que a veces requieren segunda opinión — y si vos tenés pacientes que necesiten ese nivel de planificación, podría ser útil tener un acuerdo informal. Sin compromiso — solo explorar. ¿Te paso mi tarjeta?

---

## 2. MOMS_HIDROBABY (use for HidroBaby chain + pregnant/mom businesses)

> Hola [NOMBRE], Dra. Gabriella González Pane, odontóloga en Mburucuyá. Vi que [NOMBRE_NEGOCIO] ([CIUDAD]) trabaja con mamás y embarazos. Tengo un servicio que quizá les interese saber: limpieza dental + plan de cuidados orales durante embarazo (con protocolo escrito para entregar a tus clientas). ¿Te interesaría que les derive clientas HidroBaby que necesiten esa atención con un 15% de descuento? Sin costo para ustedes, solo derivación cruzada. ¿Te puedo llamar 5 min mañana?

---

## 3. ATM_BRUXISMO (use for spa, kinesio, fisio, yoga — pain/dolor mandibular feeders)

> Hola [NOMBRE], soy Gaby, odontóloga conservadora en Mburucuyá. Atiendo casos de ATM, bruxismo y férulas oclusales — para clientas que llegan con dolor de mandíbula o cefaleas tensionales después de tratamientos suyos. ¿Les interesaría que les derive esos casos para que USTEDES hagan la parte de spa/relajación post-ferulización? Es recíproco — yo les mando paciente, ustedes me mandan paciente. Sin contrato, solo acuerdo de café. ¿Cuándo les queda bien?

---

## 4. ESTETICA_SONRISA (use for beauty/estética/salon — sonrisa + piel cross-promo)

> Hola [NOMBRE], Dra. González Pane, odontóloga estética. Vi [NOMBRE_SALÓN] tiene [N] reseñas — felicidades. Una pregunta: ¿atendés clientas que piden blanqueamiento o sonrisa? Si querés, te ofrezco un "Paquete Sonrisa + Piel" en co-promo: cliente tuya viene a consulta sonrisa conmigo (sin compromiso), vos le das paquete facial. Las dos ganamos. Te paso un PDF con antes/después para mostrarles. ¿Te interesa?

---

## 5. GYM_BOCA_GUARD (use for high-rep gyms — athletes, contact sports, mouthguards)

> Hola [NOMBRE], Dra. González Pane. ¿[GIMNASIO] maneja atletas de contacto (rugby, MMA, fútbol, jiu-jitsu)? Hago **férulas deportivas personalizadas** — Gs 600k, vs Gs 1M en el mercado. Si te interesa, puedo ir un día a [GYM] con folleto y muestras para que tus atletas vean las opciones. Vos ganás un % por cada venta, yo gano el volumen. ¿Cuándo te queda bien para 15 min?

---

## 6. EXPAT_HOTEL (use for hotel/tourism — concierge partnership)

> Hello [NOMBRE], I'm Dr. Gabriella González Pane, a conservative dentist located in Asunción (Mburucuyá neighborhood, ~5 km from [HOTEL]). I specialize in second opinions and treatment planning, with full English fluency. I would love to be a recommended provider for [HOTEL]'s concierge — particularly for guests who need dental care during their stay. I'd be happy to provide credentials, references, and a special rate for [HOTEL] guests. Would it be possible to schedule a brief meeting with your concierge manager? Best regards, Dr. Gaby

---

## Workflow to use these

1. Open `gaby-outreach-pack.csv`
2. Sort by `priority_score` (descending)
3. For each row, use the `outreach_template` to know which message above applies
4. Open the `whatsapp_url` in a browser to send — pre-filled nothing, you copy/paste the template
5. Personalize:
   - `[NOMBRE]` = first name from a quick Google search if available
   - `[N]` = `google_reviews` column
   - `[NOMBRE_NEGOCIO]` = `business_name`
   - `[CIUDAD]` = `city`
   - `[HOTEL]` = `business_name`
   - `[GIMNASIO]` = `business_name`

6. Send — Kiki does first 10/day (don't blast), wait for replies, mark in CSV with new column "status"

---

## Cadence

- **Week 1**: First 10 in priority order — test response rate
- **Week 2**: If ≥2 responses, do 30 more; if <2, change message angle
- **Week 3-4**: Adapt templates based on what got replies
- **Month 2**: Second-opinion-specific pitches to anyone who replied with interest

---

## What NOT to do

- Don't contact anyone in `DIRECT_DENTAL` play with the `ESTETICA_SONRISA` template — competitive / awkward
- Don't send to anyone without phone (column should always be populated; we filtered)
- Don't blast all 200+ on day 1 — 10/day keeps replies coming
