odoo.define('hr_lunch_kiosk.lunch_kiosk', function(require) {
  "use strict";

   var KioskMode = require('hr_attendance.kiosk_mode');
   var core = require('web.core');

   var KioskLunchMode = KioskMode.extend({
        start: function(){
            this.lunch_only = true;
            return this._super.apply(this, arguments);
        },

        _onBarcodeScanned: function(barcode) {
            var self = this;
            core.bus.off('barcode_scanned', this, this._onBarcodeScanned);
            this._rpc({
                model: 'hr.employee',
                method: 'attendance_scan',
                args: [barcode, ],
                context: {
                  'lunch_only': true,
                },
            })
            .then(function (result) {
                if (result.action) {
                    self.do_action(result.action);
                } else if (result.warning) {
                    self.do_warn(result.warning);
                    core.bus.on('barcode_scanned', self, self._onBarcodeScanned);
                }
            }, function () {
                core.bus.on('barcode_scanned', self, self._onBarcodeScanned);
            });
        },
   });


   core.action_registry.add('hr_attendance_kiosk_lunch_mode', KioskLunchMode);
});