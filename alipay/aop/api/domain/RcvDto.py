#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OuDTO import OuDTO
from alipay.aop.api.domain.FileDTO import FileDTO
from alipay.aop.api.domain.RcvLineResultOutDTO import RcvLineResultOutDTO
from alipay.aop.api.domain.PersonDTO import PersonDTO
from alipay.aop.api.domain.SupplierDTO import SupplierDTO
from alipay.aop.api.domain.WorkflowLogDTO import WorkflowLogDTO


class RcvDto(object):

    def __init__(self):
        self._company = None
        self._credit_note = None
        self._execute_amount = None
        self._files = None
        self._finish_date = None
        self._instance_id = None
        self._is_allow_modify = None
        self._po_number = None
        self._rcv_description = None
        self._rcv_detail_url = None
        self._rcv_head_id = None
        self._rcv_shipment_lines = None
        self._rcv_status = None
        self._rcv_status_code = None
        self._rcv_type = None
        self._rcv_umber = None
        self._received_amount = None
        self._receiver = None
        self._supplier_dto = None
        self._workflow_logs = None

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        if isinstance(value, OuDTO):
            self._company = value
        else:
            self._company = OuDTO.from_alipay_dict(value)
    @property
    def credit_note(self):
        return self._credit_note

    @credit_note.setter
    def credit_note(self, value):
        self._credit_note = value
    @property
    def execute_amount(self):
        return self._execute_amount

    @execute_amount.setter
    def execute_amount(self, value):
        self._execute_amount = value
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
    def finish_date(self):
        return self._finish_date

    @finish_date.setter
    def finish_date(self, value):
        self._finish_date = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def is_allow_modify(self):
        return self._is_allow_modify

    @is_allow_modify.setter
    def is_allow_modify(self, value):
        self._is_allow_modify = value
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
    def rcv_detail_url(self):
        return self._rcv_detail_url

    @rcv_detail_url.setter
    def rcv_detail_url(self, value):
        self._rcv_detail_url = value
    @property
    def rcv_head_id(self):
        return self._rcv_head_id

    @rcv_head_id.setter
    def rcv_head_id(self, value):
        self._rcv_head_id = value
    @property
    def rcv_shipment_lines(self):
        return self._rcv_shipment_lines

    @rcv_shipment_lines.setter
    def rcv_shipment_lines(self, value):
        if isinstance(value, list):
            self._rcv_shipment_lines = list()
            for i in value:
                if isinstance(i, RcvLineResultOutDTO):
                    self._rcv_shipment_lines.append(i)
                else:
                    self._rcv_shipment_lines.append(RcvLineResultOutDTO.from_alipay_dict(i))
    @property
    def rcv_status(self):
        return self._rcv_status

    @rcv_status.setter
    def rcv_status(self, value):
        self._rcv_status = value
    @property
    def rcv_status_code(self):
        return self._rcv_status_code

    @rcv_status_code.setter
    def rcv_status_code(self, value):
        self._rcv_status_code = value
    @property
    def rcv_type(self):
        return self._rcv_type

    @rcv_type.setter
    def rcv_type(self, value):
        self._rcv_type = value
    @property
    def rcv_umber(self):
        return self._rcv_umber

    @rcv_umber.setter
    def rcv_umber(self, value):
        self._rcv_umber = value
    @property
    def received_amount(self):
        return self._received_amount

    @received_amount.setter
    def received_amount(self, value):
        self._received_amount = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        if isinstance(value, PersonDTO):
            self._receiver = value
        else:
            self._receiver = PersonDTO.from_alipay_dict(value)
    @property
    def supplier_dto(self):
        return self._supplier_dto

    @supplier_dto.setter
    def supplier_dto(self, value):
        if isinstance(value, SupplierDTO):
            self._supplier_dto = value
        else:
            self._supplier_dto = SupplierDTO.from_alipay_dict(value)
    @property
    def workflow_logs(self):
        return self._workflow_logs

    @workflow_logs.setter
    def workflow_logs(self, value):
        if isinstance(value, WorkflowLogDTO):
            self._workflow_logs = value
        else:
            self._workflow_logs = WorkflowLogDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.credit_note:
            if hasattr(self.credit_note, 'to_alipay_dict'):
                params['credit_note'] = self.credit_note.to_alipay_dict()
            else:
                params['credit_note'] = self.credit_note
        if self.execute_amount:
            if hasattr(self.execute_amount, 'to_alipay_dict'):
                params['execute_amount'] = self.execute_amount.to_alipay_dict()
            else:
                params['execute_amount'] = self.execute_amount
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
        if self.finish_date:
            if hasattr(self.finish_date, 'to_alipay_dict'):
                params['finish_date'] = self.finish_date.to_alipay_dict()
            else:
                params['finish_date'] = self.finish_date
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.is_allow_modify:
            if hasattr(self.is_allow_modify, 'to_alipay_dict'):
                params['is_allow_modify'] = self.is_allow_modify.to_alipay_dict()
            else:
                params['is_allow_modify'] = self.is_allow_modify
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
        if self.rcv_detail_url:
            if hasattr(self.rcv_detail_url, 'to_alipay_dict'):
                params['rcv_detail_url'] = self.rcv_detail_url.to_alipay_dict()
            else:
                params['rcv_detail_url'] = self.rcv_detail_url
        if self.rcv_head_id:
            if hasattr(self.rcv_head_id, 'to_alipay_dict'):
                params['rcv_head_id'] = self.rcv_head_id.to_alipay_dict()
            else:
                params['rcv_head_id'] = self.rcv_head_id
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
        if self.rcv_status:
            if hasattr(self.rcv_status, 'to_alipay_dict'):
                params['rcv_status'] = self.rcv_status.to_alipay_dict()
            else:
                params['rcv_status'] = self.rcv_status
        if self.rcv_status_code:
            if hasattr(self.rcv_status_code, 'to_alipay_dict'):
                params['rcv_status_code'] = self.rcv_status_code.to_alipay_dict()
            else:
                params['rcv_status_code'] = self.rcv_status_code
        if self.rcv_type:
            if hasattr(self.rcv_type, 'to_alipay_dict'):
                params['rcv_type'] = self.rcv_type.to_alipay_dict()
            else:
                params['rcv_type'] = self.rcv_type
        if self.rcv_umber:
            if hasattr(self.rcv_umber, 'to_alipay_dict'):
                params['rcv_umber'] = self.rcv_umber.to_alipay_dict()
            else:
                params['rcv_umber'] = self.rcv_umber
        if self.received_amount:
            if hasattr(self.received_amount, 'to_alipay_dict'):
                params['received_amount'] = self.received_amount.to_alipay_dict()
            else:
                params['received_amount'] = self.received_amount
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.supplier_dto:
            if hasattr(self.supplier_dto, 'to_alipay_dict'):
                params['supplier_dto'] = self.supplier_dto.to_alipay_dict()
            else:
                params['supplier_dto'] = self.supplier_dto
        if self.workflow_logs:
            if hasattr(self.workflow_logs, 'to_alipay_dict'):
                params['workflow_logs'] = self.workflow_logs.to_alipay_dict()
            else:
                params['workflow_logs'] = self.workflow_logs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcvDto()
        if 'company' in d:
            o.company = d['company']
        if 'credit_note' in d:
            o.credit_note = d['credit_note']
        if 'execute_amount' in d:
            o.execute_amount = d['execute_amount']
        if 'files' in d:
            o.files = d['files']
        if 'finish_date' in d:
            o.finish_date = d['finish_date']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'is_allow_modify' in d:
            o.is_allow_modify = d['is_allow_modify']
        if 'po_number' in d:
            o.po_number = d['po_number']
        if 'rcv_description' in d:
            o.rcv_description = d['rcv_description']
        if 'rcv_detail_url' in d:
            o.rcv_detail_url = d['rcv_detail_url']
        if 'rcv_head_id' in d:
            o.rcv_head_id = d['rcv_head_id']
        if 'rcv_shipment_lines' in d:
            o.rcv_shipment_lines = d['rcv_shipment_lines']
        if 'rcv_status' in d:
            o.rcv_status = d['rcv_status']
        if 'rcv_status_code' in d:
            o.rcv_status_code = d['rcv_status_code']
        if 'rcv_type' in d:
            o.rcv_type = d['rcv_type']
        if 'rcv_umber' in d:
            o.rcv_umber = d['rcv_umber']
        if 'received_amount' in d:
            o.received_amount = d['received_amount']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'supplier_dto' in d:
            o.supplier_dto = d['supplier_dto']
        if 'workflow_logs' in d:
            o.workflow_logs = d['workflow_logs']
        return o


