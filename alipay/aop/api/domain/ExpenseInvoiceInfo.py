#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceOutputInfo import InvoiceOutputInfo
from alipay.aop.api.domain.OcrNormalScanInfo import OcrNormalScanInfo
from alipay.aop.api.domain.OcrPlaneScanInfo import OcrPlaneScanInfo
from alipay.aop.api.domain.OcrTaxiScanInfo import OcrTaxiScanInfo
from alipay.aop.api.domain.OcrTrainScanInfo import OcrTrainScanInfo
from alipay.aop.api.domain.VoucherFileInfo import VoucherFileInfo


class ExpenseInvoiceInfo(object):

    def __init__(self):
        self._employee_id = None
        self._invoice_output_info = None
        self._ocr_normal_scan_info = None
        self._ocr_plane_scan_info = None
        self._ocr_taxi_scan_info = None
        self._ocr_train_scan_info = None
        self._voucher_file_info = None
        self._voucher_id = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def invoice_output_info(self):
        return self._invoice_output_info

    @invoice_output_info.setter
    def invoice_output_info(self, value):
        if isinstance(value, InvoiceOutputInfo):
            self._invoice_output_info = value
        else:
            self._invoice_output_info = InvoiceOutputInfo.from_alipay_dict(value)
    @property
    def ocr_normal_scan_info(self):
        return self._ocr_normal_scan_info

    @ocr_normal_scan_info.setter
    def ocr_normal_scan_info(self, value):
        if isinstance(value, OcrNormalScanInfo):
            self._ocr_normal_scan_info = value
        else:
            self._ocr_normal_scan_info = OcrNormalScanInfo.from_alipay_dict(value)
    @property
    def ocr_plane_scan_info(self):
        return self._ocr_plane_scan_info

    @ocr_plane_scan_info.setter
    def ocr_plane_scan_info(self, value):
        if isinstance(value, OcrPlaneScanInfo):
            self._ocr_plane_scan_info = value
        else:
            self._ocr_plane_scan_info = OcrPlaneScanInfo.from_alipay_dict(value)
    @property
    def ocr_taxi_scan_info(self):
        return self._ocr_taxi_scan_info

    @ocr_taxi_scan_info.setter
    def ocr_taxi_scan_info(self, value):
        if isinstance(value, OcrTaxiScanInfo):
            self._ocr_taxi_scan_info = value
        else:
            self._ocr_taxi_scan_info = OcrTaxiScanInfo.from_alipay_dict(value)
    @property
    def ocr_train_scan_info(self):
        return self._ocr_train_scan_info

    @ocr_train_scan_info.setter
    def ocr_train_scan_info(self, value):
        if isinstance(value, OcrTrainScanInfo):
            self._ocr_train_scan_info = value
        else:
            self._ocr_train_scan_info = OcrTrainScanInfo.from_alipay_dict(value)
    @property
    def voucher_file_info(self):
        return self._voucher_file_info

    @voucher_file_info.setter
    def voucher_file_info(self, value):
        if isinstance(value, VoucherFileInfo):
            self._voucher_file_info = value
        else:
            self._voucher_file_info = VoucherFileInfo.from_alipay_dict(value)
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.invoice_output_info:
            if hasattr(self.invoice_output_info, 'to_alipay_dict'):
                params['invoice_output_info'] = self.invoice_output_info.to_alipay_dict()
            else:
                params['invoice_output_info'] = self.invoice_output_info
        if self.ocr_normal_scan_info:
            if hasattr(self.ocr_normal_scan_info, 'to_alipay_dict'):
                params['ocr_normal_scan_info'] = self.ocr_normal_scan_info.to_alipay_dict()
            else:
                params['ocr_normal_scan_info'] = self.ocr_normal_scan_info
        if self.ocr_plane_scan_info:
            if hasattr(self.ocr_plane_scan_info, 'to_alipay_dict'):
                params['ocr_plane_scan_info'] = self.ocr_plane_scan_info.to_alipay_dict()
            else:
                params['ocr_plane_scan_info'] = self.ocr_plane_scan_info
        if self.ocr_taxi_scan_info:
            if hasattr(self.ocr_taxi_scan_info, 'to_alipay_dict'):
                params['ocr_taxi_scan_info'] = self.ocr_taxi_scan_info.to_alipay_dict()
            else:
                params['ocr_taxi_scan_info'] = self.ocr_taxi_scan_info
        if self.ocr_train_scan_info:
            if hasattr(self.ocr_train_scan_info, 'to_alipay_dict'):
                params['ocr_train_scan_info'] = self.ocr_train_scan_info.to_alipay_dict()
            else:
                params['ocr_train_scan_info'] = self.ocr_train_scan_info
        if self.voucher_file_info:
            if hasattr(self.voucher_file_info, 'to_alipay_dict'):
                params['voucher_file_info'] = self.voucher_file_info.to_alipay_dict()
            else:
                params['voucher_file_info'] = self.voucher_file_info
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseInvoiceInfo()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'invoice_output_info' in d:
            o.invoice_output_info = d['invoice_output_info']
        if 'ocr_normal_scan_info' in d:
            o.ocr_normal_scan_info = d['ocr_normal_scan_info']
        if 'ocr_plane_scan_info' in d:
            o.ocr_plane_scan_info = d['ocr_plane_scan_info']
        if 'ocr_taxi_scan_info' in d:
            o.ocr_taxi_scan_info = d['ocr_taxi_scan_info']
        if 'ocr_train_scan_info' in d:
            o.ocr_train_scan_info = d['ocr_train_scan_info']
        if 'voucher_file_info' in d:
            o.voucher_file_info = d['voucher_file_info']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


