CREATE POLICY admin_manage_users
ON users
FOR ALL
USING (
clinic_id = current_setting('app.current_clinic_id')::uuid
AND current_setting('app.current_role') = 'admin'
);