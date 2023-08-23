#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcvApproverDto import RcvApproverDto
from alipay.aop.api.domain.FileDTO import FileDTO
from alipay.aop.api.domain.RcvLineDto import RcvLineDto
from alipay.aop.api.domain.LinkDTO import LinkDTO


class RcvCreateDto(object):

    def __init__(self):
        self._duplicate_approver = None
        self._files = None
        self._interface_source_code = None
        self._po_number = None
        self._rcv_description = None
        self._rcv_number = None
        self._rcv_shipment_lines = None
        self._source_bill_nos = None
        self._source_bills = None
        self._status = None
        self._unique_id = None

    @property
    def duplicate_approver(self):
        return self._duplicate_approver

    @duplicate_approver.setter
    def duplicate_approver(self, value):
        if isinstance(value, RcvApproverDto):
            self._duplicate_approver = value
        else:
            self._duplicate_approver = RcvApproverDto.from_alipay_dict(value)
    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        if isinstance(value, list):
            self._files = list()
            for i in value:
                if isinstance(i, FileDTO):
                    self._files.append(i)
                else:
                    self._files.append(FileDTO.from_alipay_dict(i))
    @property
    def interface_source_code(self):
        return self._interface_source_code

    @interface_source_code.setter
    def interface_source_code(self, value):
        self._interface_source_code = value
    @property
    def po_number(self):
        return self._po_number

    @po_number.setter
    def po_number(self, value):
        self._po_number = value
    @property
    def rcv_description(self):
        return self._rcv_description

    @rcv_description.setter
    def rcv_description(self, value):
        self._rcv_description = value
    @property
    def rcv_number(self):
        return self._rcv_number

    @rcv_number.setter
    def rcv_number(self, value):
        self._rcv_number = value
    @property
    def rcv_shipment_lines(self):
        return self._rcv_shipment_lines

    @rcv_shipment_lines.setter
    def rcv_shipment_lines(self, value):
        if isinstance(value, list):
            self._rcv_shipment_lines = list()
            for i in value:
                if isinstance(i, RcvLineDto):
                    self._rcv_shipment_lines.append(i)
                else:
                    self._rcv_shipment_lines.append(RcvLineDto.from_alipay_dict(i))
    @property
    def source_bill_nos(self):
        return self._source_bill_nos

    @source_bill_nos.setter
    def source_bill_nos(self, value):
        if isinstance(value, list):
            self._source_bill_nos = list()
            for i in value:
                self._source_bill_nos.append(i)
    @property
    def source_bills(self):
        return self._source_bills

    @source_bills.setter
    def source_bills(self, value):
        if isinstance(value, list):
            self._source_bills = list()
            for i in value:
                if isinstance(i, LinkDTO):
                    self._source_bills.append(i)
                else:
                    self._source_bills.append(LinkDTO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.duplicate_approver:
            if hasattr(self.duplicate_approver, 'to_alipay_dict'):
                params['duplicate_approver'] = self.duplicate_approver.to_alipay_dict()
            else:
                params['duplicate_approver'] = self.duplicate_approver
        if self.files:
            if isinstance(self.files, list):
                for i in range(0, len(self.files)):
                    element = self.files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.files[i] = element.to_alipay_dict()
            if hasattr(self.files, 'to_alipay_dict'):
                params['files'] = self.files.to_alipay_dict()
            else:
                params['files'] = self.files
        if self.interface_source_code:
            if hasattr(self.interface_source_code, 'to_alipay_dict'):
                params['interface_source_code'] = self.interface_source_code.to_alipay_dict()
            else:
                params['interface_source_code'] = self.interface_source_code
        if self.po_number:
            if hasattr(self.po_number, 'to_alipay_dict'):
                params['po_number'] = self.po_number.to_alipay_dict()
            else:
                params['po_number'] = self.po_number
        if self.rcv_description:
            if hasattr(self.rcv_description, 'to_alipay_dict'):
                params['rcv_description'] = self.rcv_description.to_alipay_dict()
            else:
                params['rcv_description'] = self.rcv_description
        if self.rcv_number:
            if hasattr(self.rcv_number, 'to_alipay_dict'):
                params['rcv_number'] = self.rcv_number.to_alipay_dict()
            else:
                params['rcv_number'] = self.rcv_number
        if self.rcv_shipment_lines:
            if isinstance(self.rcv_shipment_lines, list):
                for i in range(0, len(self.rcv_shipment_lines)):
                    element = self.rcv_shipment_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rcv_shipment_lines[i] = element.to_alipay_dict()
            if hasattr(self.rcv_shipment_lines, 'to_alipay_dict'):
                params['rcv_shipment_lines'] = self.rcv_shipment_lines.to_alipay_dict()
            else:
                params['rcv_shipment_lines'] = self.rcv_shipment_lines
        if self.source_bill_nos:
            if isinstance(self.source_bill_nos, list):
                for i in range(0, len(self.source_bill_nos)):
                    element = self.source_bill_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_bill_nos[i] = element.to_alipay_dict()
            if hasattr(self.source_bill_nos, 'to_alipay_dict'):
                params['source_bill_nos'] = self.source_bill_nos.to_alipay_dict()
            else:
                params['source_bill_nos'] = self.source_bill_nos
        if self.source_bills:
            if isinstance(self.source_bills, list):
                for i in range(0, len(self.source_bills)):
                    element = self.source_bills[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_bills[i] = element.to_alipay_dict()
            if hasattr(self.source_bills, 'to_alipay_dict'):
                params['source_bills'] = self.source_bills.to_alipay_dict()
            else:
                params['source_bills'] = self.source_bills
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcvCreateDto()
        if 'duplicate_approver' in d:
            o.duplicate_approver = d['duplicate_approver']
        if 'files' in d:
            o.files = d['files']
        if 'interface_source_code' in d:
            o.interface_source_code = d['interface_source_code']
        if 'po_number' in d:
            o.po_number = d['po_number']
        if 'rcv_description' in d:
            o.rcv_description = d['rcv_description']
        if 'rcv_number' in d:
            o.rcv_number = d['rcv_number']
        if 'rcv_shipment_lines' in d:
            o.rcv_shipment_lines = d['rcv_shipment_lines']
        if 'source_bill_nos' in d:
            o.source_bill_nos = d['source_bill_nos']
        if 'source_bills' in d:
            o.source_bills = d['source_bills']
        if 'status' in d:
            o.status = d['status']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


