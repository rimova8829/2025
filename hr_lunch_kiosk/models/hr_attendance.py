from odoo import fields, models, api, exceptions, _


class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    @api.model
    def attendance_scan(self, barcode):
        if self._context.get('lunch_only'):
            employee = self.sudo().search([('barcode', '=', barcode)], limit=1)
            if employee:
                if employee.attendance_state == 'checked_in':
                    employee = employee.with_context(state='lunch_start')

                elif employee.attendance_state == 'lunch_start':
                    employee = employee.with_context(state='lunch_end')

                elif employee.attendance_state == 'lunch_end':
                    return {'warning': _("You can Not Checkout From Here")}

                else:
                    return {'warning': _("You Must Check In First")}

                return employee._attendance_action(
                    'hr_lunch_kiosk.hr_attendance_action_kiosk_lunch_mode')
            return {
                'warning': _("No employee corresponding to Badge ID '%(barcode)s.'") % {
                    'barcode': barcode}}
        return super().attendance_scan(barcode)

    def _attendance_action(self, next_action):
        res = super()._attendance_action(next_action)
        if self._context.get('lunch_only'):
            res['action']['tag'] = 'hr_attendance_lunch_greeting_message'
            res['action']['emp_data'] = self.read([])[0]
        return res