function template(strings, ...keys) {
    return (function (...values) {
        let dict = values[values.length - 1] || {};
        let result = [strings[0]];
        keys.forEach(function (key, i) {
            let value = Number.isInteger(key) ? values[key] : dict[key];
            result.push(value, strings[i + 1]);
        });
        return result.join('');
    });
}

let attribute_block = template`
    <hr>
    <div class="row">
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">STR:</span>
                </div>
                <input type="number" class="form-control" id="inv-str" value=${0} readonly>
                <input type="text" readonly class="form-control" value=${1}>
                <input type="text" readonly class="form-control" value=${2}>
            </div>
        </div>
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">DEX:</span>
                </div>
                <input type="number" class="form-control" id="inv-dex" value=${3} readonly>
                <input type="text" readonly class="form-control" value=${4}>
                <input type="text" readonly class="form-control" value=${5}>
            </div>
        </div>
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">POW:</span>
                </div>
                <input type="number" class="form-control" id="inv-pow" value=${6} readonly>
                <input type="text" readonly class="form-control" value=${7}>
                <input type="text" readonly class="form-control" value=${8}>
            </div>
        </div>
    </div >
    <hr>
    <div class="row">
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">CON:</span>
                </div>
                <input type="number" class="form-control" id="inv-con" value=${9} readonly>
                <input type="text" readonly class="form-control" value=${10}>
                <input type="text" readonly class="form-control" value=${11}>
            </div>
        </div >

        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">APP:</span>
                </div>
                <input type="number" class="form-control" id="inv-app" value=${12} readonly>
                <input type="text" readonly class="form-control" value=${13}>
                <input type="text" readonly class="form-control" value=${14}>
            </div>
        </div >

        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">EDU:</span>
                </div>
                <input type="number" class="form-control" id="inv-edu" value=${15} readonly>
                <input type="text" readonly class="form-control" value=${16}>
                <input type="text" readonly class="form-control" value=${17}>
            </div>
        </div >
    </div>
    <hr>
    <div class="row">
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">SIZ:</span>
                </div>
                <input type="number" class="form-control" id="inv-siz" value=${18} readonly>
                <input type="text" readonly class="form-control" value=${19}>
                <input type="text" readonly class="form-control" value=${20}>
            </div>
        </div >
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">INT:</span>
                </div>
                <input type="number" class="form-control" id="inv-int" value=${21} readonly>
                <input type="text" readonly class="form-control" value=${22}>
                <input type="text" readonly class="form-control" value=${23}>
            </div>
        </div >
        <div class="col">
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="">MOV:</span>
                </div>
                <input type="text" readonly class="form-control" id="inv-mov" value=${24} disabled>
            </div>
        </div>
    </div>`;

function attribute_seeder(attributes) {
    return attribute_block(
        attributes.STR[0] > 9 ? attributes.STR[0] : "0" + attributes.STR[0],
        attributes.STR[1] > 9 ? attributes.STR[1] : "0" + attributes.STR[1],
        attributes.STR[2] > 9 ? attributes.STR[2] : "0" + attributes.STR[2],

        attributes.DEX[0] > 9 ? attributes.DEX[0] : "0" + attributes.DEX[0],
        attributes.DEX[1] > 9 ? attributes.DEX[1] : "0" + attributes.DEX[1],
        attributes.DEX[2] > 9 ? attributes.DEX[2] : "0" + attributes.DEX[2],

        attributes.POW[0] > 9 ? attributes.POW[0] : "0" + attributes.POW[0],
        attributes.POW[1] > 9 ? attributes.POW[1] : "0" + attributes.POW[1],
        attributes.POW[2] > 9 ? attributes.POW[2] : "0" + attributes.POW[2],

        attributes.CON[0] > 9 ? attributes.CON[0] : "0" + attributes.CON[0],
        attributes.CON[1] > 9 ? attributes.CON[1] : "0" + attributes.CON[1],
        attributes.CON[2] > 9 ? attributes.CON[2] : "0" + attributes.CON[2],

        attributes.APP[0] > 9 ? attributes.APP[0] : "0" + attributes.APP[0],
        attributes.APP[1] > 9 ? attributes.APP[1] : "0" + attributes.APP[1],
        attributes.APP[2] > 9 ? attributes.APP[2] : "0" + attributes.APP[2],

        attributes.EDU[0] > 9 ? attributes.EDU[0] : "0" + attributes.EDU[0],
        attributes.EDU[1] > 9 ? attributes.EDU[1] : "0" + attributes.EDU[1],
        attributes.EDU[2] > 9 ? attributes.EDU[2] : "0" + attributes.EDU[2],

        attributes.SIZ[0] > 9 ? attributes.SIZ[0] : "0" + attributes.SIZ[0],
        attributes.SIZ[1] > 9 ? attributes.SIZ[1] : "0" + attributes.SIZ[1],
        attributes.SIZ[2] > 9 ? attributes.SIZ[2] : "0" + attributes.SIZ[2],

        attributes.INT[0] > 9 ? attributes.INT[0] : "0" + attributes.INT[0],
        attributes.INT[1] > 9 ? attributes.INT[1] : "0" + attributes.INT[1],
        attributes.INT[2] > 9 ? attributes.INT[2] : "0" + attributes.INT[2],

        attributes.MOV
    )
}

export function update_attribute(res) {
    let attributes_name = {
        'inv-str': 'strength',
        'inv-con': 'constitution',
        'inv-pow': 'power',
        'inv-siz': 'size',
        'inv-edu': 'education',
        'inv-int': 'intelligence',
        'inv-app': 'appearance',
        'inv-dex': 'dexterity'
    }
    $("#inv-attrs div div input[id^='inv-']").change(
        function (evt) {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            let id_ = evt.target.id;
            let data = {};
            data[attributes_name[id_]] = $("#" + id_).val();
            $.ajax({
                url: window.location.pathname + '/attrs/update',
                type: "POST",
                data: data,
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (res) {
                    $("#" + id_).val(res[attributes_name[id_]][0])
                    let siblings = $("#" + id_).siblings('input');
                    siblings[0].value = res[attributes_name[id_]][1];
                    siblings[1].value = res[attributes_name[id_]][2];
                }
            })
        });
}


export function parse_attributes(res) {
    let attributes = res.attributes;
    $("#inv-attrs").children().remove();
    $("#inv-extra-attr").children().remove();
    $("#inv-attrs").append(
        attribute_seeder(attributes)
    );
    $("#inv-extra-attr").append(
        `<div class="col">
            Build: <b>${attributes.BUILD[1]} </b>
        </div >
        <div class="col offset-md-7">
            Damage Bonus: <b>${attributes.BUILD[0]}</b>
        </div>`
    )

    update_attribute();

    $("#inv-attrs-edit").click(
        function (evt) {
            if ($("#inv-attrs-edit")[0].innerHTML === `<i class="bi bi-unlock"></i>`) {
                $("#inv-attrs div div input[id^='inv-']").prop('readonly', false);
                $("#inv-attrs-edit")[0].innerHTML = `<i class="bi bi-lock"></i>`
            } else {
                $("#inv-attrs div div input[id^='inv-']").prop('readonly', true);
                $("#inv-attrs-edit")[0].innerHTML = `<i class="bi bi-unlock"></i>`
            }
        }
    )
}