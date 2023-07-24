#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuClaimRecordVo(object):

    def __init__(self):
        self._accident_date = None
        self._accident_reason = None
        self._claim_no = None
        self._close_date = None
        self._err_code = None
        self._err_msg = None
        self._fallback_date = None
        self._fallback_reason = None
        self._insurant_birthday = None
        self._insurant_id_code = None
        self._insurant_id_type = None
        self._insurant_name = None
        self._insurant_sex = None
        self._insurant_type = None
        self._insure_name = None
        self._is_submit = None
        self._notice_download_url = None
        self._paid_amount = None
        self._refuse_mark = None
        self._refuse_reason = None
        self._register_date = None
        self._relate_birth_date = None
        self._relate_insurant_id_code = None
        self._relate_insurant_id_type = None
        self._relate_insurant_name = None
        self._relate_sex = None
        self._report_biz_no = None
        self._report_date = None
        self._report_no = None
        self._source = None
        self._status = None
        self._supplier_id = None
        self._sync_method = None

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
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def close_date(self):
        return self._close_date

    @close_date.setter
    def close_date(self, value):
        self._close_date = value
    @property
    def err_code(self):
        return self._err_code

    @err_code.setter
    def err_code(self, value):
        self._err_code = value
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def fallback_date(self):
        return self._fallback_date

    @fallback_date.setter
    def fallback_date(self, value):
        self._fallback_date = value
    @property
    def fallback_reason(self):
        return self._fallback_reason

    @fallback_reason.setter
    def fallback_reason(self, value):
        self._fallback_reason = value
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
    def insure_name(self):
        return self._insure_name

    @insure_name.setter
    def insure_name(self, value):
        self._insure_name = value
    @property
    def is_submit(self):
        return self._is_submit

    @is_submit.setter
    def is_submit(self, value):
        self._is_submit = value
    @property
    def notice_download_url(self):
        return self._notice_download_url

    @notice_download_url.setter
    def notice_download_url(self, value):
        self._notice_download_url = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def refuse_mark(self):
        return self._refuse_mark

    @refuse_mark.setter
    def refuse_mark(self, value):
        self._refuse_mark = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
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
    def report_biz_no(self):
        return self._report_biz_no

    @report_biz_no.setter
    def report_biz_no(self, value):
        self._report_biz_no = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
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
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def sync_method(self):
        return self._sync_method

    @sync_method.setter
    def sync_method(self, value):
        self._sync_method = value


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
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.close_date:
            if hasattr(self.close_date, 'to_alipay_dict'):
                params['close_date'] = self.close_date.to_alipay_dict()
            else:
                params['close_date'] = self.close_date
        if self.err_code:
            if hasattr(self.err_code, 'to_alipay_dict'):
                params['err_code'] = self.err_code.to_alipay_dict()
            else:
                params['err_code'] = self.err_code
        if self.err_msg:
            if hasattr(self.err_msg, 'to_alipay_dict'):
                params['err_msg'] = self.err_msg.to_alipay_dict()
            else:
                params['err_msg'] = self.err_msg
        if self.fallback_date:
            if hasattr(self.fallback_date, 'to_alipay_dict'):
                params['fallback_date'] = self.fallback_date.to_alipay_dict()
            else:
                params['fallback_date'] = self.fallback_date
        if self.fallback_reason:
            if hasattr(self.fallback_reason, 'to_alipay_dict'):
                params['fallback_reason'] = self.fallback_reason.to_alipay_dict()
            else:
                params['fallback_reason'] = self.fallback_reason
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
        if self.insure_name:
            if hasattr(self.insure_name, 'to_alipay_dict'):
                params['insure_name'] = self.insure_name.to_alipay_dict()
            else:
                params['insure_name'] = self.insure_name
        if self.is_submit:
            if hasattr(self.is_submit, 'to_alipay_dict'):
                params['is_submit'] = self.is_submit.to_alipay_dict()
            else:
                params['is_submit'] = self.is_submit
        if self.notice_download_url:
            if hasattr(self.notice_download_url, 'to_alipay_dict'):
                params['notice_download_url'] = self.notice_download_url.to_alipay_dict()
            else:
                params['notice_download_url'] = self.notice_download_url
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.refuse_mark:
            if hasattr(self.refuse_mark, 'to_alipay_dict'):
                params['refuse_mark'] = self.refuse_mark.to_alipay_dict()
            else:
                params['refuse_mark'] = self.refuse_mark
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
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
        if self.report_biz_no:
            if hasattr(self.report_biz_no, 'to_alipay_dict'):
                params['report_biz_no'] = self.report_biz_no.to_alipay_dict()
            else:
                params['report_biz_no'] = self.report_biz_no
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
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
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.sync_method:
            if hasattr(self.sync_method, 'to_alipay_dict'):
                params['sync_method'] = self.sync_method.to_alipay_dict()
            else:
                params['sync_method'] = self.sync_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuClaimRecordVo()
        if 'accident_date' in d:
            o.accident_date = d['accident_date']
        if 'accident_reason' in d:
            o.accident_reason = d['accident_reason']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'close_date' in d:
            o.close_date = d['close_date']
        if 'err_code' in d:
            o.err_code = d['err_code']
        if 'err_msg' in d:
            o.err_msg = d['err_msg']
        if 'fallback_date' in d:
            o.fallback_date = d['fallback_date']
        if 'fallback_reason' in d:
            o.fallback_reason = d['fallback_reason']
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
        if 'insure_name' in d:
            o.insure_name = d['insure_name']
        if 'is_submit' in d:
            o.is_submit = d['is_submit']
        if 'notice_download_url' in d:
            o.notice_download_url = d['notice_download_url']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'refuse_mark' in d:
            o.refuse_mark = d['refuse_mark']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'register_date' in d:
            o.register_date = d['register_date']
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
        if 'report_biz_no' in d:
            o.report_biz_no = d['report_biz_no']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'sync_method' in d:
            o.sync_method = d['sync_method']
        return o


