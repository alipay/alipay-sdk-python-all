#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumeOutputInfo import ConsumeOutputInfo
from alipay.aop.api.domain.InvoiceOutputInfo import InvoiceOutputInfo
from alipay.aop.api.domain.OcrNormalScanInfo import OcrNormalScanInfo
from alipay.aop.api.domain.OcrPlaneScanInfo import OcrPlaneScanInfo
from alipay.aop.api.domain.OcrTaxiScanInfo import OcrTaxiScanInfo
from alipay.aop.api.domain.OcrTrainScanInfo import OcrTrainScanInfo


class PackageItemOpenInfo(object):

    def __init__(self):
        self._consume_output_info = None
        self._file_download_url = None
        self._file_type = None
        self._invoice_output_info = None
        self._item_source = None
        self._item_sub_type = None
        self._item_type = None
        self._ocr_normal_scan_info = None
        self._ocr_plane_scan_info = None
        self._ocr_taxi_scan_info = None
        self._ocr_train_scan_info = None

    @property
    def consume_output_info(self):
        return self._consume_output_info

    @consume_output_info.setter
    def consume_output_info(self, value):
        if isinstance(value, ConsumeOutputInfo):
            self._consume_output_info = value
        else:
            self._consume_output_info = ConsumeOutputInfo.from_alipay_dict(value)
    @property
    def file_download_url(self):
        return self._file_download_url

    @file_download_url.setter
    def file_download_url(self, value):
        self._file_download_url = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
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
    def item_source(self):
        return self._item_source

    @item_source.setter
    def item_source(self, value):
        self._item_source = value
    @property
    def item_sub_type(self):
        return self._item_sub_type

    @item_sub_type.setter
    def item_sub_type(self, value):
        self._item_sub_type = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.consume_output_info:
            if hasattr(self.consume_output_info, 'to_alipay_dict'):
                params['consume_output_info'] = self.consume_output_info.to_alipay_dict()
            else:
                params['consume_output_info'] = self.consume_output_info
        if self.file_download_url:
            if hasattr(self.file_download_url, 'to_alipay_dict'):
                params['file_download_url'] = self.file_download_url.to_alipay_dict()
            else:
                params['file_download_url'] = self.file_download_url
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.invoice_output_info:
            if hasattr(self.invoice_output_info, 'to_alipay_dict'):
                params['invoice_output_info'] = self.invoice_output_info.to_alipay_dict()
            else:
                params['invoice_output_info'] = self.invoice_output_info
        if self.item_source:
            if hasattr(self.item_source, 'to_alipay_dict'):
                params['item_source'] = self.item_source.to_alipay_dict()
            else:
                params['item_source'] = self.item_source
        if self.item_sub_type:
            if hasattr(self.item_sub_type, 'to_alipay_dict'):
                params['item_sub_type'] = self.item_sub_type.to_alipay_dict()
            else:
                params['item_sub_type'] = self.item_sub_type
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PackageItemOpenInfo()
        if 'consume_output_info' in d:
            o.consume_output_info = d['consume_output_info']
        if 'file_download_url' in d:
            o.file_download_url = d['file_download_url']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'invoice_output_info' in d:
            o.invoice_output_info = d['invoice_output_info']
        if 'item_source' in d:
            o.item_source = d['item_source']
        if 'item_sub_type' in d:
            o.item_sub_type = d['item_sub_type']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'ocr_normal_scan_info' in d:
            o.ocr_normal_scan_info = d['ocr_normal_scan_info']
        if 'ocr_plane_scan_info' in d:
            o.ocr_plane_scan_info = d['ocr_plane_scan_info']
        if 'ocr_taxi_scan_info' in d:
            o.ocr_taxi_scan_info = d['ocr_taxi_scan_info']
        if 'ocr_train_scan_info' in d:
            o.ocr_train_scan_info = d['ocr_train_scan_info']
        return o


