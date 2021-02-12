export function get_attributes(res) {
    let attributes = res.attributes;
    $("#inv-attrs").append(
        `<div class="col">
            <div class="row">
                <div class="col">STR:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.STR[0] > 10 ? attributes.STR[0] : "0" + attributes.STR[0]}</b>|
                    <b>${attributes.STR[1] > 10 ? attributes.STR[1] : "0" + attributes.STR[1]}</b>|
                    <b>${attributes.STR[2] > 10 ? attributes.STR[2] : "0" + attributes.STR[2]}</b>
                </div >
            </div >
            <div class="row">
                <div class="col">CON:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.CON[0] > 10 ? attributes.CON[0] : "0" + attributes.CON[0]}</b>|
                    <b>${attributes.CON[1] > 10 ? attributes.CON[1] : "0" + attributes.CON[1]}</b>|
                    <b>${attributes.CON[2] > 10 ? attributes.CON[2] : "0" + attributes.CON[2]}</b>
                </div >
            </div >
            <div class="row">
                <div class="col">SIZ:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.SIZ[0] > 10 ? attributes.SIZ[0] : "0" + attributes.SIZ[0]}</b>|
                    <b>${attributes.SIZ[1] > 10 ? attributes.SIZ[1] : "0" + attributes.SIZ[1]}</b>|
                    <b>${attributes.SIZ[2] > 10 ? attributes.SIZ[2] : "0" + attributes.SIZ[2]}</b>
                </div >
            </div >
        </div >
        <div class="col">
            <div class="row">
                <div class="col">DEX:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.DEX[0] > 10 ? attributes.DEX[0] : "0" + attributes.DEX[0]}</b>|
                    <b>${attributes.DEX[1] > 10 ? attributes.DEX[1] : "0" + attributes.DEX[1]}</b>|
                    <b>${attributes.DEX[2] > 10 ? attributes.DEX[2] : "0" + attributes.DEX[2]}</b>
                </div>
            </div>
            <div class="row">
                <div class="col">APP:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.APP[0] > 10 ? attributes.APP[0] : "0" + attributes.APP[0]}</b>|
                    <b>${attributes.APP[1] > 10 ? attributes.APP[1] : "0" + attributes.APP[1]}</b>|
                    <b>${attributes.APP[2] > 10 ? attributes.APP[2] : "0" + attributes.APP[2]}</b>
                </div>
            </div>
            <div class="row">
                <div class="col">INT:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.INT[0] > 10 ? attributes.INT[0] : "0" + attributes.INT[0]}</b>|
                    <b>${attributes.INT[1] > 10 ? attributes.INT[1] : "0" + attributes.INT[1]}</b>|
                    <b>${attributes.INT[2] > 10 ? attributes.INT[2] : "0" + attributes.INT[2]}</b>
                </div>
            </div>
        </div>
        <div class="col">
            <div class="row">
                <div class="col">POW:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.POW[0] > 10 ? attributes.POW[0] : "0" + attributes.POW[0]}</b>|
                    <b>${attributes.POW[1] > 10 ? attributes.POW[1] : "0" + attributes.POW[1]}</b>|
                    <b>${attributes.POW[2] > 10 ? attributes.POW[2] : "0" + attributes.POW[2]}</b>
                </div>
            </div>
            <div class="row">
                <div class="col">EDU:</div>
                <div style="text-align: right" class="col">
                    <b>${attributes.EDU[0] > 10 ? attributes.EDU[0] : "0" + attributes.EDU[0]}</b>|
                    <b>${attributes.EDU[1] > 10 ? attributes.EDU[1] : "0" + attributes.EDU[1]}</b>|
                    <b>${attributes.EDU[2] > 10 ? attributes.EDU[2] : "0" + attributes.EDU[2]}</b>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    MOV:
                </div>
                <div style="text-align: right" class="col">
                    <b>${attributes.MOV}</b>
                </div>
            </div>
        </div>`
    );
    $("#inv-extra-attr").append(
        `<div class="col">
            Build: <b>${attributes.BUILD[1]} </b>
        </div >
        <div class="col offset-md-7">
            Damage Bonus: <b>${attributes.BUILD[0]}</b>
        </div>`
    )
}