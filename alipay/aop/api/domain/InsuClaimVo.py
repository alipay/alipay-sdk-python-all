#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsuClaimAttachmentVo import InsuClaimAttachmentVo


class InsuClaimVo(object):

    def __init__(self):
        self._accident_date = None
        self._accident_reason = None
        self._attachment_url = None
        self._claim_attachment_vo = None
        self._claim_flag = None
        self._contact_email = None
        self._employee_id = None
        self._insurant_birthday = None
        self._insurant_id_code = None
        self._insurant_id_type = None
        self._insurant_name = None
        self._insurant_sex = None
        self._insurant_type = None
        self._is_submit = None
        self._pay_account_bank = None
        self._pay_account_no = None
        self._pay_name = None
        self._pay_type = None
        self._pay_type_code = None
        self._relate_birth_date = None
        self._relate_insurant_id_code = None
        self._relate_insurant_id_type = None
        self._relate_insurant_name = None
        self._relate_sex = None
        self._report_amount = None
        self._report_biz_no = None
        self._report_no = None
        self._source = None
        self._status = None

    @property
    def accident_date(self):
        return self._accident_date

    @accident_date.setter
    def accident_date(self, value):
        self._accident_date = value
    @property
    def accident_reason(self):
        return self._accident_reason

    @accident_reason.setter
    def accident_reason(self, value):
        self._accident_reason = value
    @property
    def attachment_url(self):
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, value):
        if isinstance(value, list):
            self._attachment_url = list()
            for i in value:
                self._attachment_url.append(i)
    @property
    def claim_attachment_vo(self):
        return self._claim_attachment_vo

    @claim_attachment_vo.setter
    def claim_attachment_vo(self, value):
        if isinstance(value, InsuClaimAttachmentVo):
            self._claim_attachment_vo = value
        else:
            self._claim_attachment_vo = InsuClaimAttachmentVo.from_alipay_dict(value)
    @property
    def claim_flag(self):
        return self._claim_flag

    @claim_flag.setter
    def claim_flag(self, value):
        self._claim_flag = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def insurant_birthday(self):
        return self._insurant_birthday

    @insurant_birthday.setter
    def insurant_birthday(self, value):
        self._insurant_birthday = value
    @property
    def insurant_id_code(self):
        return self._insurant_id_code

    @insurant_id_code.setter
    def insurant_id_code(self, value):
        self._insurant_id_code = value
    @property
    def insurant_id_type(self):
        return self._insurant_id_type

    @insurant_id_type.setter
    def insurant_id_type(self, value):
        self._insurant_id_type = value
    @property
    def insurant_name(self):
        return self._insurant_name

    @insurant_name.setter
    def insurant_name(self, value):
        self._insurant_name = value
    @property
    def insurant_sex(self):
        return self._insurant_sex

    @insurant_sex.setter
    def insurant_sex(self, value):
        self._insurant_sex = value
    @property
    def insurant_type(self):
        return self._insurant_type

    @insurant_type.setter
    def insurant_type(self, value):
        self._insurant_type = value
    @property
    def is_submit(self):
        return self._is_submit

    @is_submit.setter
    def is_submit(self, value):
        self._is_submit = value
    @property
    def pay_account_bank(self):
        return self._pay_account_bank

    @pay_account_bank.setter
    def pay_account_bank(self, value):
        self._pay_account_bank = value
    @property
    def pay_account_no(self):
        return self._pay_account_no

    @pay_account_no.setter
    def pay_account_no(self, value):
        self._pay_account_no = value
    @property
    def pay_name(self):
        return self._pay_name

    @pay_name.setter
    def pay_name(self, value):
        self._pay_name = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def pay_type_code(self):
        return self._pay_type_code

    @pay_type_code.setter
    def pay_type_code(self, value):
        self._pay_type_code = value
    @property
    def relate_birth_date(self):
        return self._relate_birth_date

    @relate_birth_date.setter
    def relate_birth_date(self, value):
        self._relate_birth_date = value
    @property
    def relate_insurant_id_code(self):
        return self._relate_insurant_id_code

    @relate_insurant_id_code.setter
    def relate_insurant_id_code(self, value):
        self._relate_insurant_id_code = value
    @property
    def relate_insurant_id_type(self):
        return self._relate_insurant_id_type

    @relate_insurant_id_type.setter
    def relate_insurant_id_type(self, value):
        self._relate_insurant_id_type = value
    @property
    def relate_insurant_name(self):
        return self._relate_insurant_name

    @relate_insurant_name.setter
    def relate_insurant_name(self, value):
        self._relate_insurant_name = value
    @property
    def relate_sex(self):
        return self._relate_sex

    @relate_sex.setter
    def relate_sex(self, value):
        self._relate_sex = value
    @property
    def report_amount(self):
        return self._report_amount

    @report_amount.setter
    def report_amount(self, value):
        self._report_amount = value
    @property
    def report_biz_no(self):
        return self._report_biz_no

    @report_biz_no.setter
    def report_biz_no(self, value):
        self._report_biz_no = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.accident_date:
            if hasattr(self.accident_date, 'to_alipay_dict'):
                params['accident_date'] = self.accident_date.to_alipay_dict()
            else:
                params['accident_date'] = self.accident_date
        if self.accident_reason:
            if hasattr(self.accident_reason, 'to_alipay_dict'):
                params['accident_reason'] = self.accident_reason.to_alipay_dict()
            else:
                params['accident_reason'] = self.accident_reason
        if self.attachment_url:
            if isinstance(self.attachment_url, list):
                for i in range(0, len(self.attachment_url)):
                    element = self.attachment_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_url[i] = element.to_alipay_dict()
            if hasattr(self.attachment_url, 'to_alipay_dict'):
                params['attachment_url'] = self.attachment_url.to_alipay_dict()
            else:
                params['attachment_url'] = self.attachment_url
        if self.claim_attachment_vo:
            if hasattr(self.claim_attachment_vo, 'to_alipay_dict'):
                params['claim_attachment_vo'] = self.claim_attachment_vo.to_alipay_dict()
            else:
                params['claim_attachment_vo'] = self.claim_attachment_vo
        if self.claim_flag:
            if hasattr(self.claim_flag, 'to_alipay_dict'):
                params['claim_flag'] = self.claim_flag.to_alipay_dict()
            else:
                params['claim_flag'] = self.claim_flag
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.insurant_birthday:
            if hasattr(self.insurant_birthday, 'to_alipay_dict'):
                params['insurant_birthday'] = self.insurant_birthday.to_alipay_dict()
            else:
                params['insurant_birthday'] = self.insurant_birthday
        if self.insurant_id_code:
            if hasattr(self.insurant_id_code, 'to_alipay_dict'):
                params['insurant_id_code'] = self.insurant_id_code.to_alipay_dict()
            else:
                params['insurant_id_code'] = self.insurant_id_code
        if self.insurant_id_type:
            if hasattr(self.insurant_id_type, 'to_alipay_dict'):
                params['insurant_id_type'] = self.insurant_id_type.to_alipay_dict()
            else:
                params['insurant_id_type'] = self.insurant_id_type
        if self.insurant_name:
            if hasattr(self.insurant_name, 'to_alipay_dict'):
                params['insurant_name'] = self.insurant_name.to_alipay_dict()
            else:
                params['insurant_name'] = self.insurant_name
        if self.insurant_sex:
            if hasattr(self.insurant_sex, 'to_alipay_dict'):
                params['insurant_sex'] = self.insurant_sex.to_alipay_dict()
            else:
                params['insurant_sex'] = self.insurant_sex
        if self.insurant_type:
            if hasattr(self.insurant_type, 'to_alipay_dict'):
                params['insurant_type'] = self.insurant_type.to_alipay_dict()
            else:
                params['insurant_type'] = self.insurant_type
        if self.is_submit:
            if hasattr(self.is_submit, 'to_alipay_dict'):
                params['is_submit'] = self.is_submit.to_alipay_dict()
            else:
                params['is_submit'] = self.is_submit
        if self.pay_account_bank:
            if hasattr(self.pay_account_bank, 'to_alipay_dict'):
                params['pay_account_bank'] = self.pay_account_bank.to_alipay_dict()
            else:
                params['pay_account_bank'] = self.pay_account_bank
        if self.pay_account_no:
            if hasattr(self.pay_account_no, 'to_alipay_dict'):
                params['pay_account_no'] = self.pay_account_no.to_alipay_dict()
            else:
                params['pay_account_no'] = self.pay_account_no
        if self.pay_name:
            if hasattr(self.pay_name, 'to_alipay_dict'):
                params['pay_name'] = self.pay_name.to_alipay_dict()
            else:
                params['pay_name'] = self.pay_name
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.pay_type_code:
            if hasattr(self.pay_type_code, 'to_alipay_dict'):
                params['pay_type_code'] = self.pay_type_code.to_alipay_dict()
            else:
                params['pay_type_code'] = self.pay_type_code
        if self.relate_birth_date:
            if hasattr(self.relate_birth_date, 'to_alipay_dict'):
                params['relate_birth_date'] = self.relate_birth_date.to_alipay_dict()
            else:
                params['relate_birth_date'] = self.relate_birth_date
        if self.relate_insurant_id_code:
            if hasattr(self.relate_insurant_id_code, 'to_alipay_dict'):
                params['relate_insurant_id_code'] = self.relate_insurant_id_code.to_alipay_dict()
            else:
                params['relate_insurant_id_code'] = self.relate_insurant_id_code
        if self.relate_insurant_id_type:
            if hasattr(self.relate_insurant_id_type, 'to_alipay_dict'):
                params['relate_insurant_id_type'] = self.relate_insurant_id_type.to_alipay_dict()
            else:
                params['relate_insurant_id_type'] = self.relate_insurant_id_type
        if self.relate_insurant_name:
            if hasattr(self.relate_insurant_name, 'to_alipay_dict'):
                params['relate_insurant_name'] = self.relate_insurant_name.to_alipay_dict()
            else:
                params['relate_insurant_name'] = self.relate_insurant_name
        if self.relate_sex:
            if hasattr(self.relate_sex, 'to_alipay_dict'):
                params['relate_sex'] = self.relate_sex.to_alipay_dict()
            else:
                params['relate_sex'] = self.relate_sex
        if self.report_amount:
            if hasattr(self.report_amount, 'to_alipay_dict'):
                params['report_amount'] = self.report_amount.to_alipay_dict()
            else:
                params['report_amount'] = self.report_amount
        if self.report_biz_no:
            if hasattr(self.report_biz_no, 'to_alipay_dict'):
                params['report_biz_no'] = self.report_biz_no.to_alipay_dict()
            else:
                params['report_biz_no'] = self.report_biz_no
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuClaimVo()
        if 'accident_date' in d:
            o.accident_date = d['accident_date']
        if 'accident_reason' in d:
            o.accident_reason = d['accident_reason']
        if 'attachment_url' in d:
            o.attachment_url = d['attachment_url']
        if 'claim_attachment_vo' in d:
            o.claim_attachment_vo = d['claim_attachment_vo']
        if 'claim_flag' in d:
            o.claim_flag = d['claim_flag']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'insurant_birthday' in d:
            o.insurant_birthday = d['insurant_birthday']
        if 'insurant_id_code' in d:
            o.insurant_id_code = d['insurant_id_code']
        if 'insurant_id_type' in d:
            o.insurant_id_type = d['insurant_id_type']
        if 'insurant_name' in d:
            o.insurant_name = d['insurant_name']
        if 'insurant_sex' in d:
            o.insurant_sex = d['insurant_sex']
        if 'insurant_type' in d:
            o.insurant_type = d['insurant_type']
        if 'is_submit' in d:
            o.is_submit = d['is_submit']
        if 'pay_account_bank' in d:
            o.pay_account_bank = d['pay_account_bank']
        if 'pay_account_no' in d:
            o.pay_account_no = d['pay_account_no']
        if 'pay_name' in d:
            o.pay_name = d['pay_name']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'pay_type_code' in d:
            o.pay_type_code = d['pay_type_code']
        if 'relate_birth_date' in d:
            o.relate_birth_date = d['relate_birth_date']
        if 'relate_insurant_id_code' in d:
            o.relate_insurant_id_code = d['relate_insurant_id_code']
        if 'relate_insurant_id_type' in d:
            o.relate_insurant_id_type = d['relate_insurant_id_type']
        if 'relate_insurant_name' in d:
            o.relate_insurant_name = d['relate_insurant_name']
        if 'relate_sex' in d:
            o.relate_sex = d['relate_sex']
        if 'report_amount' in d:
            o.report_amount = d['report_amount']
        if 'report_biz_no' in d:
            o.report_biz_no = d['report_biz_no']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        return o


