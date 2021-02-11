function skills_load() {
    $(document).ready(
        $.ajax({
            url: "{% url 'inv_skills' res.investigator.uuid %}",
            success: function (res) {
                let id_ = "#skills_1";
                for (skill of res.skills) {
                    let full_val = skill[1] < 10 ? "0" + skill[1] : skill[1];
                    let half_val = skill[2] < 10 ? "0" + skill[2] : skill[2];
                    let fifth_val = skill[3] < 10 ? "0" + skill[3] : skill[3];
                    if (res.skills.indexOf(skill) === 0) {
                        $("#inv-skills").append(
                            `<div class="col" id="skills_1"></div>`
                        );
                    } else if (res.skills.indexOf(skill) === 35) {
                        id_ = "#skills_2";
                        $("#inv-skills").append(
                            `<div class="col" id="skills_2"></div>`
                        );
                    }
                    else if (res.skills.indexOf(skill) === 71) {
                        id_ = "#skills_3";
                        $("#inv-skills").append(
                            `<div class="col" id="skills_3"></div>`
                        );
                    };
                    $(id_).append(
                        `
                    <div class="row">
                        <div class="col">
                            ${skill[0]}:
                        </div >
                        <div style="text-align: right" class="col">
                            <b>${full_val}</b >|
                            <b>${half_val}</b > |
                            <b>${fifth_val}</b>
                        </div >
                    </div >`
                    )
                }
            },
            error: function (res) {
                console.log(res);
            }
        })
    )
}
skills_load();